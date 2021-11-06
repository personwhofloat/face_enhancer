'''
@paper: GAN Prior Embedded Network for Blind Face Restoration in the Wild (CVPR2021)
@author: yangxy (yangtao9009@gmail.com)
'''
import os
import cv2
import glob
import time
import numpy as np
from PIL import Image
import __init_paths
from face_model.face_gan import FaceGAN

class FaceColorization(object):
    def __init__(self, base_dir='./', size=1024, model='GPEN-Colorization-1024', channel_multiplier=2):
        self.facegan = FaceGAN(base_dir, size, model, channel_multiplier)

    # make sure the face image is well aligned. Please refer to face_enhancement.py
    def process(self, gray):
        # colorize the face
        out = self.facegan.process(gray)

        return out
