from cs285.infrastructure import pytorch_util as ptu
from .base_exploration_model import BaseExplorationModel
import torch.optim as optim
from torch import nn
import torch

def init_method_1(model):
    model.weight.data.uniform_()
    model.bias.data.uniform_()

def init_method_2(model):
    model.weight.data.normal_()
    model.bias.data.normal_()


class RNDModel(nn.Module, BaseExplorationModel):
    def __init__(self, hparams, optimizer_spec, **kwargs):
        super().__init__(**kwargs)
        self.ob_dim = hparams['ob_dim']
        self.output_size = hparams['rnd_output_size']
        self.n_layers = hparams['rnd_n_layers']
        self.size = hparams['rnd_size']
        self.optimizer_spec = optimizer_spec

        # <TODO>: Create two neural networks:
        # 1) f, the random function we are trying to learn
        # 2) f_hat, the function we are using to learn f
        # 3) Initialize networks differently (f with normal, and f_hat with uniform)
        # <TEST>: Switch the initializations
        # <TEST>: Add range to uniform distribution
        self.f = ptu.build_mlp(
                input_size=self.ob_dim,
                output_size=self.output_size,
                n_layers=self.n_layers,
                size=self.size,
                init_method=init_method_2,
            )
        self.f_hat = ptu.build_mlp(
                input_size=self.ob_dim,
                output_size=self.output_size,
                n_layers=self.n_layers,
                size=self.size,
                init_method=init_method_1,
            )

        # <TODO>: Create the optimizer with the learning rate schedule
        self.optimizer = self.optimizer_spec.constructor(
            self.f_hat.parameters(),
            **self.optimizer_spec.optim_kwargs
        )
        self.learning_rate_scheduler = optim.lr_scheduler.LambdaLR(
            self.optimizer,
            self.optimizer_spec.learning_rate_schedule,
        )

        # <TODO>: Cast to device
        self.f.to(ptu.device)
        self.f_hat.to(ptu.device)

    def forward(self, ob_no):
        # <TODO>: Get the prediction error for ob_no
        # HINT: Remember to detach the output of self.f!
        predictions_f = self.f(ob_no).detach()
        predictions_f_hat = self.f_hat(ob_no)
        pred_err_n = torch.linalg.norm(predictions_f - predictions_f_hat, dim=1)
        return pred_err_n

    def forward_np(self, ob_no):
        ob_no = ptu.from_numpy(ob_no)
        error = self(ob_no)
        return ptu.to_numpy(error)

    def update(self, ob_no):
        # <TODO>: Cast to device
        ob_no = ptu.from_numpy(ob_no)

        # <TODO>: Update f_hat using ob_no
        # Hint: Take the mean prediction error across the batch
        pred_err_n = self(ob_no)
        loss = torch.mean(pred_err_n)

        self.optimizer.zero_grad()
        loss.backward()
        # <TEST>: Add gradient clipping
        # utils.clip_grad_value_(self.f_hat.parameters(), hparams['grad_norm_clipping'])
        self.optimizer.step()
        
        self.learning_rate_scheduler.step()

        return ptu.to_numpy(loss)
