 # -*- coding:utf-8 -*-
import numpy as np
from PIL import Image

img = Image.open("010004.png")
imgdata = np.unique(img)
print(imgdata)
print(imgdata.dtype)
#print(imgdata.channels)  ##tongdao shu

img2 = Image.open("010009.png")
imgdata2 = np.unique(img2)
print(imgdata2)
print(imgdata2.dtype)
