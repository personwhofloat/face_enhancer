import os.path
import logging
import torch
# from utils import utils_model
from .models.network_rrdbnet import RRDBNet

'''
model = net(in_nc=3, out_nc=3, nf=64, nb=23, gc=32, sf=4)  # define network
model.load_state_dict(torch.load("BSRGAN.pth"))
model.eval()
'''
