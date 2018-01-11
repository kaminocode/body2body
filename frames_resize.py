import cv2
import argparse
import os
from PIL import Image
import numpy as np
import re
import sys
import math
import time
import scipy
import matplotlib
from torch import np
import pylab as plt
from joblib import Parallel, delayed
import util
import torch
import torch as T
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
from collections import OrderedDict
from config_reader import config_reader
from scipy.ndimage.filters import gaussian_filter

parser = argparse.ArgumentParser(description='train or test')
parser.add_argument('type', metavar='N', type=str, nargs='+',help='whether test or train')
args = parser.parse_args()




#reading frames from the video
vidcap = cv2.VideoCapture(str(args.type[0])+'.mp4')
success,image = vidcap.read()
count = 0
success = True
if not os.path.exists(str(args.type[0])+"_frames"):
    os.makedirs(str(args.type[0])+"_frames")
    os.makedirs(str(args.type[0])+"_frames/org_frames")
    os.makedirs(str(args.type[0])+"_frames/pose_frames")
	
print('Reading frames')
while success:
  success,image = vidcap.read()
  #print('Read a new frame: ', success)
  cv2.imwrite(str(args.type[0])+"_frames/org_frames/%d.png" % count, image)     # save frame as JPEG file
  count += 1
os.remove(str(args.type[0])+"_frames/org_frames/"+str(count-1)+".png")








#resizing the frames to 256x256
def load_images_from_folder(folder):
	images = []
	i=0
	print('Resizing frames to 720x720')
	for q in range(len(os.listdir(folder))):
		filename=str(q)+".png"
		img = Image.open(os.path.join(folder,filename))
		basewidth = 720
		wpercent = (basewidth/float(img.size[1]))
		hsize = int((float(img.size[1])*float(wpercent)))
		img = img.resize((hsize,basewidth), Image.ANTIALIAS)
		width, height = img.size   # Get dimensions
		new_width=720
		new_height=720
		left = (width - new_width)/2
		top = (height - new_height)/2
		right = (width + new_width)/2
		bottom = (height + new_height)/2
		img.crop((left, top, right, bottom))
		img.save(str(args.type[0])+'_frames/org_frames/'+str(i)+'.png')		
		#print(i)
		i=i+1	
	return images

load_images_from_folder("./"+str(args.type[0])+"_frames/org_frames")

