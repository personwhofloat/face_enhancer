import argparse
import cv2
import glob
import numpy as np
import os
import torch
from basicsr.utils import imwrite

from gfpgan import GFPGANer

'''model = GFPGANer(
           model_path= 'GFPGAN.pth',
           upscale=2,
           arch='clean',
           channel_multiplier=2
        )
        '''
