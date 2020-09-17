# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 23:24:43 2020

@author: Matador
"""

import numpy as np
import cv2
import os
folder = 'resources'
file = 'lena.jpg'
face = 'haarcascade_frontalface_default.xml'

path = os.path.join(folder, file)
facepath = os.path.join(folder,face)

faceCascade =  cv2.CascadeClassifier(facepath)

img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(img_gray,1.1,4)

for (x, y, w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow('lena',img)