# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:20:53 2020

@author: Matador
"""

import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

folder = 'resources'
file = 'chichiro.jpg'

path = os.path.join(folder,file)

img = cv2.imread(path)

cv2.imshow('chichiro',img)
plt.imshow(img)


width = 200
heigth = 200
pts1 = np.float32([[350,200],[368,261],[520,226],[521,342]])
pts2 = np.float32([[0,0],[width,0], [0,heigth],[width,heigth]])

img2 = cv2.getPerspectiveTransform(pts1,pts2,img)