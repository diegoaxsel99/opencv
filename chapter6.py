# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:42:09 2020

@author: Matador
"""

# juntar imagenes

import cv2 
import numpy as np
import os

folder = 'resources'
file = 'chichiro.jpg'
file2 = 'la_puta.jpg'

path = os.path.join(folder,file)
path2 = os.path.join(folder,file2)

img = cv2.imread(path)
img2 = cv2.imread(path2)

img3 = np.hstack((img,img2[0:img.shape[0],:]))

cv2.imshow('imagen doble',img3)

