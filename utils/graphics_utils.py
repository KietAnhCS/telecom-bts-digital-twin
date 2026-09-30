import torch
import math
import numpy as np 
from typing import NamedTuple 

class BasicPointCloud(NameTuple):


def geom_transform_points():
    pass 

def getWorld2View(R,t):
    pass 
def getWorld2View2(R, t, translate=np.array([.0, .0, .0]), scale=1.0):
    pass

def getProjectionMatrix(znear, zfar, fovX, fovY):
    pass

def fov2focal(fov, pixels):
    pass 

def focal2fov(focal, pixels):
    pass