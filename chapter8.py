# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 14:18:40 2020

@author: Matador
"""

import numpy as np
import cv2
import os


def getcontours(img,copy):
    
    contour, hirarchys = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for conts in contour:
        area = cv2.contourArea(conts)
        
        if(area >100):
            cv2.drawContours(copy,conts,-1,(255,0,0),3)
            peri = cv2.arcLength(conts,True)
            
            k = 0.02
            aprox = cv2.approxPolyDP(conts,k*peri,True)
            
                # print(len(aprox))
            
            objcor = len(aprox)
            
            x,y, w, h = cv2.boundingRect(aprox)
            
            cv2.rectangle(copy,(x,y),(x+w,y+h),(0,0,255),3)
            
            
        
folder = 'resources'
file = 'figuras.jpg'

path = os.path.join(folder,file)

img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray,100,255)
img_blank = np.zeros_like(img)
copy = img.copy()

getcontours(edges,copy)

cv2.imshow('figuras',copy)