# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 17:59:12 2020

@author: Matador
"""

import numpy as np
import cv2
import os

# detecion de colores

def empty(a):
    pass


cap = cv2.VideoCapture(0)


space = "Trackbar"

cv2.namedWindow(space)
cv2.resizeWindow(space,1000,640)

names = ["hue min","hue max","sat min","sat max","val min","val max"]
v_max = [179,179,255, 255, 255, 255]
v_min = [0,179,0,255,0,255]
values = {}

for i in range(len(names)):
    cv2.createTrackbar(names[i],space,v_min[i],v_max[i],empty)
    values[names[i]] = 0

while True:
    
    sucess, img = cap.read()
    
    for i in range(len(names)):
        values[names[i]] = (cv2.getTrackbarPos(names[i], space))
    
    lower = np.array([values["hue min"],values["sat min"], values["val min"]])
    upper = np.array([values["hue max"],values["sat max"], values["val max"]])
    
    img_hsv = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
    
    mask = cv2.inRange(img_hsv,lower,upper)
    result = cv2.bitwise_and(img,img,mask = mask)
    
    cv2.imshow('la puta',np.hstack((img,img_hsv)))
    
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break