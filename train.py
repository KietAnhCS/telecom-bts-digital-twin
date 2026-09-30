160-419
SADGS/train.py:160-419 (precompute structure tensor, vòng lặp train, khối densify 316-403).

import torch 
import numpy as np
import os, random, time 
from random import randint 
from lpipsPyTorch import lpip
from utils.loss_utils import l1_loss,l2_loss, get_multiscale_structure_tensor_v1, get_multiscale_structure_tensor_v2
from fused_ssim import fused_ssim as fast_ssim 
from gaussian_renderer import render_strucgs, network_gui_ws 
import sys 
from scene import Scene, GaussianModel 
from utils.sh_utils import RGB2SH
from utils.general_utils import safe_state 
import uuid 
from tqdm import tqdm 
from utils.image_utils import psnr 
from argparse import ArgumentParser, Namespace 
from arguments import ModelParams, PipelineParams, OptimizationParams

try:
    from torch.utils.tensorboard import SummaryWriter
    TENSORBOARD_FOUND = True 
except ImportError:
    TENSORBOARD_FOUND = False 

from utils.freq_utils import sampling_cameras, update_freq_stats_online 
import torch.nn.functional as F 


def training(dataset, apt, pipe, testing_iterations, saving_iterations, checkpoint_iterations, checkpoint, debug_from, websocker, ply_path, prune_iterations):
    first_iter = 0 
    tb_writer = prepare_output_and_logger(database)
    gaussians = GaussianModel(dataset.sh_degree, opt.optimizer_type)

def prepare_output_and_logger(args):
    pass
def training_report(tb_writter, iteration, Ll1, loss, l1_loss, elapsed, testing_iteration, scene : Scene, renderFunc, renderArgs):

if __name__ == "__main__":
    # Set up command line argument parser 
    parser = ArgumentParser(description="Training script parameters")
    lp = ModelParams(parser)
    op = OptimizationParams(parser)
    pp = PipelineParams(parser)
    parser.add_argument()
    args.save_iteration.append(args.iterations)

    print("Optimizing" + args.model_path)

    # Initialize system state (RNG)
    safe_state(args.quiet)

    if(args.websockets):
        network_gui_ws.init(args.ip, args.port)
    torch.autograd.set_detect_anomaly(args.detect_anomaly)

    training(
        lp.extract(args),
        op.extract(args),
        pp.extract(args),
        args.test_iterations,
        args.save_iterations,
        args.checkpoint_iterations,
        args.start_checkpoint,
        args.debug_from,
        args.websockets,
        args.ply_path,
        args.prune_iterations
    )

    # All done
    print("\nTraining complete")