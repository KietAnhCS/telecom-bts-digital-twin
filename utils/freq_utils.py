1-419
SADGS/utils/freq_utils.py:1-419 (sampling_cameras, get_loss, compute_photometric_loss, compute_projected_axes_subset:116-178, update_freq_stats_online:181-418).

import torch
import torch.nn.functional as F
from PIL import ImageFilter 
from gaussian_renderer import render_strucgs 
from .loss_utils import l1_loss, frequency_loss_simple, get_multiscale_structure_tensor_torch
from fused_ssim import fused_ssim as fast_ssim 
import torchvision.transforms as transforms 
from utils.general_utils import build_rotation
import random 

def sampling_cameras(my_viewpoint_stack, mode="fps", num_cams=60, weights=None):

def get_loss(reconstructed_image, original_image):

def compute_photometric_loss(viewpoint_cam, image):

def compute_projected_axes_subset(means2D, depths, scales, rotations, viewpoint_camera):

def update_freq_stats_online(viewpoint_cam, gaussians, cov2D, visibility_filter, structure_tensor_cache, viewspace_point_tensor=None, grad_threshold=None, transmittance_threshold=0.0, opacity_threshold=0.05, eta_compute_mode="wavelength"):