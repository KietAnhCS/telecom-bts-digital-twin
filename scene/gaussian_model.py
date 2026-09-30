import torch
import numpy as np 
from utils.general_utils import inverse_sigmoid, get_expon_lr_func, build_rotation, identity_gate
from torch import nn 
import os 
from util.system_utils import mkdir_p
from utils.sh_utils import RGB2SH
from simple_knn._C import distCUDA2
from utils.graphics_utils import BasicPointCloud 
from utils.general_utils import strip_sysmetric, build_scaling_rotation

try:
    from diff_gaussian_rasterization_strucgs import SparseGaussianAdam 
except: 
    pass

class GaussianModel:

    def setup_function(self):
        pass

    def modify_function():
        pass

    def __init__():
        pass

    def capture():
        pass

    def restore(): 
        pass

    def get_scaling(self):
        pass

    def get_scaling_with_3D_filter(self):
        pass

    def get_rotation(self):
        pass

    def get_xyz(self):
        pass

    def get_features(self):
        pass

    def get_features_dc(self):
        pass

    def get_features_rest(self):
        pass

    def get_opacity(self):
        pass

    def get_opacity_with_3d_filter(self):
        pass

    def get_convariance():
        pass

    def compute_3D_filter(self, cameras):
        pass

    def oneupSHdegree(self):
        pass

    def create_from_pcd():
        pass

    def training_setup():
        pass

    def update_learning_rate():
        pass

    def optimizer_step():
        pass

    def construct_list_of_attributes(self):
        pass

    def save_ply():
        pass

    def reset_opacity():
        pass

    def load_ply():
        pass

    def replace_tensor_to_optimizer():
        pass

    def _prune_optimizer(seft, mask):
        pass

    def prunt_points(self, mask):
        pass

    def cat_tensor_to_optimizer(seft, tensor_dict):
        pass

    def densification_postfix():
        pass

    def densify_and_split_structgs(self, metric_mask, max_eta_3ch=None, scale_power=1.0):
        pass

    def expand_undersized_gs():
        pass

    def densify_and_split():
        pass

    def densify_and_clone():
        pass

    def densify_and_prune():
        pass

    def densify_and_clone_strucgs():
        pass

    def densify_and_prune_strucgs():
        pass

    def add_densification_stats(seft, viewspace_point_tensor, update_filter):
        pass

    def final_prune_strucgs(self, min_opacity, pruning_score = None):
        pass