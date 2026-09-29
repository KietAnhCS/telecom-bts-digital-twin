170-387
(get_structure_tensor_torch, get_multiscale_structure_tensor_v1, get_multiscale_structure_tensor_v2, frequency_loss_simple).

import torch 
import torch.nn.functional as F
import torchvision
from torch.autograd import Variable 
from math import exp, sqrt

def get_structure_tensor_torch(image_tensor, sigma=1.0, rho=1.0):
    """
    Computes Multi-Channel Structure Tensor (Di Zenzo's Method).
    Summing energy across RGB channels avoids missing iso-luminant edges.
    """
def get_multiscale_structure_tensor_v1(image_tensor, levels=3, base_sigma=1., octave_step=1.5, smoothing_factor=1.0, power_factor=3.0, aggregation_mode='average'):
    
    
def get_multiscale_structure_tensor_v2(image_tensor, sigma=1.0, rho=1.0):
    """
    Computes a True Multi-scale Structure Tensor.
    Unlike v1, this version computes the structure tensor at each scale level
    based on the blurred image at that level, rather than blurring a pre-computed
    base tensor. This properly captures orientation and frequency at each scale.
    """