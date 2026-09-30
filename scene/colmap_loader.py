import numpy as np 
import collections
import struct 

CameraModel = collections.namedtuple()
Camera = collections.namedtuple()
BaseImage = collections.namedtuple()
Point3D = collections.namedtuple() 

CAMERA_MODELS = {

}
CAMERA_MODEL_IDS = dict([])
CAMERA_MODEL_NAMEDS = dict([])

def qvec2rotmat(qvec):
    pass

def rotmap2qvec(R):
    pass 

class Image(BaseImage):
    def qvecrotmat(seft):
        pass 


def read_next_bytes():
    oass 

def read_points3D_text(path):
    pass 

def read_points3D_binary(path_to_model_file):
    pass 

def read_intrinsics_text(path):
    pass 

def read_extrinsics_binary():
    pass 

def read_intrinsics_binary():
    pass 

def read_extrinsics_text(path):
    pass 

def read_colmap_bin_array(path):
    pass 