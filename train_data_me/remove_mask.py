#!usr/bin/python
# -*- coding:utf-8 -*-
import PIL.Image
import numpy as np
import cv2
import os
from PIL import Image
from skimage import io,data,color
import matplotlib.pyplot as plt


for i in range(0,10):
	img = PIL.Image.open("/home/zhulifu/Desktop/maskrcnnn_tupianyuchuli/train_data/labelme_json/01000%d_json/label.png" %i)
	img = np.array(img)
	dst = Image.fromarray(np.uint8(img))
	
	dst.save("/home/zhulifu/Desktop/maskrcnnn_tupianyuchuli/train_data/cv2_mask/01000%d.png"%i)


for i in range(10,100):
	img = PIL.Image.open("/home/zhulifu/Desktop/maskrcnnn_tupianyuchuli/train_data/labelme_json/0100%d_json/label.png" %i)
	img = np.array(img)
	
	dst = Image.fromarray(np.uint8(img))
	dst.save("/home/zhulifu/Desktop/maskrcnnn_tupianyuchuli/train_data/cv2_mask/0100%d.png"%i)


for i in range(100,151):
	img = PIL.Image.open("/home/zhulifu/Desktop/maskrcnnn_tupianyuchuli/train_data/labelme_json/010%d_json/label.png" %i)
	img = np.array(img)
	dst = Image.fromarray(np.uint8(img))
	
	dst.save("/home/zhulifu/Desktop/maskrcnnn_tupianyuchuli/train_data/cv2_mask/010%d.png"%i)
