from collections import OrderedDict

from cs285.critics.dqn_critic import DQNCritic
from cs285.critics.cql_critic import CQLCritic
from cs285.infrastructure.replay_buffer import ReplayBuffer
from cs285.infrastructure.utils import *
from cs285.infrastructure import pytorch_util as ptu
from cs285.policies.argmax_policy import ArgMaxPolicy
from cs285.infrastructure.dqn_utils import MemoryOptimizedReplayBuffer
from cs285.exploration.rnd_model import RNDModel
from .dqn_agent import DQNAgent
from cs285.policies.MLP_policy import MLPPolicyAWAC
import numpy as np
import torch


class AWACAgent(DQNAgent):
    def __init__(self, env, agent_params, normalize_rnd=True, rnd_gamma=0.99):
        super(AWACAgent, self).__init__(env, agent_params)
        
        self.replay_buffer = MemoryOptimizedReplayBuffer(100000, 1, float_obs=True)
        self.num_exploration_steps = agent_params['num_exploration_steps']
        self.offline_exploitation = agent_params['offline_exploitation']

        self.exploitation_critic = DQNCritic(agent_params, self.optimizer_spec)
        self.exploration_critic = DQNCritic(agent_params, self.optimizer_spec)
        
        self.exploration_model = RNDModel(agent_params, self.optimizer_spec)
        self.explore_weight_schedule = agent_params['explore_weight_schedule']
        self.exploit_weight_schedule = agent_params['exploit_weight_schedule']

        # <TEST>: Change to exploration_critic
        # self.actor = ArgMaxPolicy(self.exploitation_critic)
        self.actor = ArgMaxPolicy(self.exploration_critic)
        self.eval_policy = self.awac_actor = MLPPolicyAWAC(
            self.agent_params['ac_dim'],
            self.agent_params['ob_dim'],
            self.agent_params['n_layers'],
            self.agent_params['size'],
            self.agent_params['discrete'],
            self.agent_params['learning_rate'],
            self.agent_params['awac_lambda'],
        )

        self.exploit_rew_shift = agent_params['exploit_rew_shift']
        self.exploit_rew_scale = agent_params['exploit_rew_scale']
        self.eps = agent_params['eps']

        self.running_rnd_rew_std = 1
        self.normalize_rnd = normalize_rnd
        self.rnd_gamma = rnd_gamma

    def get_qvals(self, critic, obs, action):
        # TODO: get q-value for a given critic, obs, and action
        qa_values = critic.q_net(obs)
        q_value = torch.gather(qa_values, 1, action.unsqueeze(1)).squeeze(1)
        return q_value

    def estimate_advantage(self, ob_no, ac_na, re_n, next_ob_no, terminal_n, n_actions=10):
        # TODO: Calculate and return the advantage (n sample estimate) 
        # TODO convert to torch tensors
        sum_path_lengths = len(ob_no)
        ob_no = ptu.from_numpy(ob_no)
        ac_na = ptu.from_numpy(ac_na).to(torch.long)
        re_n = ptu.from_numpy(re_n)
        next_ob_no = ptu.from_numpy(next_ob_no)
        terminal_n = ptu.from_numpy(terminal_n)

        # HINT: store computed values in the provided vals list. You will use the average of this list for calculating the advantage.
        vals = []
        # TODO: get action distribution for current obs, you will use this for the value function estimate
        dist = self.awac_actor(ob_no)
        # TODO Calculate Value Function Estimate given current observation
        # HINT: You may find it helpful to utilze get_qvals defined above
        if self.agent_params['discrete']:
            for i in range(self.agent_params['ac_dim']):
                # <TEST>: Use self.exploitation_critic instead of self.actor.critic (same for L88)
                actions = torch.full((sum_path_lengths,), i, dtype=torch.long)
                q_val_i = self.get_qvals(self.exploitation_critic, ob_no, actions)
                prob_i = torch.exp(dist.log_prob(actions))
                vals.append(q_val_i * prob_i)
        else:
            
            for _ in range(n_actions):
                pass
        v_pi = sum(vals)

        # TODO Calculate Q-Values
        q_vals = self.get_qvals(self.exploitation_critic, ob_no, ac_na)
        # TODO Calculate the Advantage using q_vals and v_pi  
        return ptu.to_numpy(q_vals - v_pi)

    def train(self, ob_no, ac_na, re_n, next_ob_no, terminal_n):
        log = {}

        # <TEST>: Shift to below the next if-statement.
        # At t = num_exploration_steps + 1, the batch is from the exploration critic,
        # but the critic used for advantage will be exploitation critic.
        if self.t > self.num_exploration_steps:
            # TODO: After exploration is over, set the actor to optimize the extrinsic critic
            #HINT: Look at method ArgMaxPolicy.set_critic
            self.actor.set_critic(self.exploitation_critic)

        if (self.t > self.learning_starts
                and self.t % self.learning_freq == 0
                and self.replay_buffer.can_sample(self.batch_size)
        ):
            # TODO: Get Reward Weights
            # Get the current explore reward weight and exploit reward weight
            #       using the schedule's passed in (see __init__)
            # COMMENT: Until part 3, explore_weight = 1, and exploit_weight = 0
            explore_weight = self.explore_weight_schedule.value(self.t)
            exploit_weight = self.exploit_weight_schedule.value(self.t)


            # TODO: Run Exploration Model #
            # Evaluate the exploration model on s to get the exploration bonus
            # HINT: Normalize the exploration bonus, as RND values vary highly in magnitude
            pred_error = self.exploration_model.forward_np(ob_no)
            expl_bonus = normalize(pred_error, 0.0, self.running_rnd_rew_std)
            self.running_rnd_rew_std = self.rnd_gamma * self.running_rnd_rew_std + (1 - self.rnd_gamma) * np.std(pred_error)

            # TODO: Reward Calculations #
            # Calculate mixed rewards, which will be passed into the exploration critic
            # HINT: See doc for definition of mixed_reward
            mixed_reward = explore_weight * expl_bonus + exploit_weight * re_n

            # TODO: Calculate the environment reward
            # HINT: For part 1, env_reward is just 're_n'
            #       After this, env_reward is 're_n' shifted by self.exploit_rew_shift,
            #       and scaled by self.exploit_rew_scale
            env_reward = (re_n + self.exploit_rew_shift) * self.exploit_rew_scale

            # TODO: Update Critics And Exploration Model #
            # 1): Update the exploration model (based off s')
            # 2): Update the exploration critic (based off mixed_reward)
            # 3): Update the exploitation critic (based off env_reward)
            expl_model_loss = self.exploration_model.update(next_ob_no)
            exploration_critic_loss = self.exploration_critic.update(ob_no, ac_na, next_ob_no, mixed_reward, terminal_n)
            exploitation_critic_loss = self.exploitation_critic.update(ob_no, ac_na, next_ob_no, env_reward, terminal_n)

            # TODO: update actor
            # 1): Estimate the advantage, detach advantage
            # 2): Calculate the awac actor loss
            advantage = self.estimate_advantage(ob_no, ac_na, re_n, next_ob_no, terminal_n)
            actor_loss = self.awac_actor.update(ob_no, ac_na, advantage)

            # TODO: Update Target Networks #
            if self.num_param_updates % self.target_update_freq == 0:
                #  Update the exploitation and exploration target networks
                self.exploration_critic.update_target_network()
                self.exploitation_critic.update_target_network()

            # Logging #
            log['Exploration Critic Loss'] = exploration_critic_loss['Training Loss']
            log['Exploitation Critic Loss'] = exploitation_critic_loss['Training Loss']
            log['Exploration Model Loss'] = expl_model_loss

            # Uncomment these lines after completing awac
            log['Actor Loss'] = actor_loss

            self.num_param_updates += 1

        self.t += 1
        return log


    def step_env(self):
        """
            Step the env and store the transition
            At the end of this block of code, the simulator should have been
            advanced one step, and the replay buffer should contain one more transition.
            Note that self.last_obs must always point to the new latest observation.
        """
        if (not self.offline_exploitation) or (self.t <= self.num_exploration_steps):
            self.replay_buffer_idx = self.replay_buffer.store_frame(self.last_obs)

        perform_random_action = np.random.random() < self.eps or self.t < self.learning_starts

        if perform_random_action:
            action = self.env.action_space.sample()
        else:
            processed = self.replay_buffer.encode_recent_observation()
            action = self.actor.get_action(processed)

        next_obs, reward, done, info = self.env.step(action)
        self.last_obs = next_obs.copy()

        if (not self.offline_exploitation) or (self.t <= self.num_exploration_steps):
            self.replay_buffer.store_effect(self.replay_buffer_idx, action, reward, done)

        if done:
            self.last_obs = self.env.reset()
