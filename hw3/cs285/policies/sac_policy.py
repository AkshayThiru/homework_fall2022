from cs285.policies.MLP_policy import MLPPolicy
import torch
import numpy as np
from cs285.infrastructure import sac_utils
from cs285.infrastructure import pytorch_util as ptu
from torch import nn
from torch import optim
# from torch.distributions import transformed_distribution as trans_dist
import itertools

class MLPPolicySAC(MLPPolicy):
    def __init__(self,
                 ac_dim,
                 ob_dim,
                 n_layers,
                 size,
                 discrete=False,
                 learning_rate=3e-4,
                 training=True,
                 log_std_bounds=[-20,2],
                 action_range=[-1,1],
                 init_temperature=1.0,
                 **kwargs
                 ):
        super(MLPPolicySAC, self).__init__(ac_dim, ob_dim, n_layers, size, discrete, learning_rate, training, **kwargs)
        self.log_std_bounds = log_std_bounds
        self.action_range = action_range
        self.init_temperature = init_temperature
        self.learning_rate = learning_rate

        self.log_alpha = torch.tensor(np.log(self.init_temperature)).to(ptu.device)
        self.log_alpha.requires_grad = True
        self.log_alpha_optimizer = torch.optim.Adam([self.log_alpha], lr=self.learning_rate)

        self.target_entropy = -ac_dim

    @property
    def alpha(self):
        # TODO: Formulate entropy term
        entropy = torch.exp(self.log_alpha)

        return entropy

    def get_action(self, obs: np.ndarray, sample=True) -> np.ndarray:
        # TODO: return sample from distribution if sampling
        # if not sampling return the mean of the distribution
        observation = ptu.from_numpy(obs)
        ac_dist = self(observation)

        if sample:
            action = ac_dist.rsample()
        else:
            action = ac_dist.mean

        action = ptu.to_numpy(action)

        if len(action.shape) > 1:
            action = action
        else:
            action = action[np.newaxis, :]

        return action

    # This function defines the forward pass of the network.
    # You can return anything you want, but you should be able to differentiate
    # through it. For example, you can return a torch.FloatTensor. You can also
    # return more flexible objects, such as a
    # `torch.distributions.Distribution` object. It's up to you!
    def forward(self, observation: torch.FloatTensor):
        # TODO: Implement pass through network, computing logprobs and apply correction for Tanh squashing

        # HINT: 
        # You will need to clip log values
        # You will need SquashedNormal from sac_utils file 
        ac_mean = self.mean_net(observation)
        # clip std using log_std_bounds and .clip
        ac_std = torch.exp(torch.clamp(self.logstd, min=self.log_std_bounds[0], max=self.log_std_bounds[1]))
        # pass through SquashedNormal
        action_distribution = sac_utils.SquashedNormal(ac_mean, ac_std, self.action_range)

        return action_distribution

    def update(self, obs, critic):
        # TODO Update actor network and entropy regularizer
        # return losses and alpha value
        observation = ptu.from_numpy(obs)

        ac_dist = self(observation)
        actions = ac_dist.rsample()
        ac_log_prob = torch.sum(ac_dist.log_prob(actions), 1)
        actor_loss = self.alpha * ac_log_prob - torch.mean(critic(observation, actions), 1)
        actor_loss = torch.mean(actor_loss)

        self.optimizer.zero_grad()
        actor_loss.backward()
        # torch.nn.utils.clip_grad_value_(
        #     itertools.chain([self.logstd], self.mean_net.parameters()),
        #     10000
        #     )
        self.optimizer.step()

        # update alpha.
        if torch.isnan(observation).any():
            print(observation, '\n')

        ac_dist = self(observation)
        actions = ac_dist.rsample()
        ac_log_prob = torch.sum(ac_dist.log_prob(actions), 1)
        alpha_loss = torch.mean(-1.0 * self.alpha * (ac_log_prob + self.target_entropy))

        self.log_alpha_optimizer.zero_grad()
        alpha_loss.backward()
        self.log_alpha_optimizer.step()

        # if torch.isnan(actor_loss):
        #     print(torch.cat((ac_dist.log_prob(actions), actions), 1))
        #     print(actor_loss, alpha_loss, '\n')

        return actor_loss, alpha_loss, self.alpha