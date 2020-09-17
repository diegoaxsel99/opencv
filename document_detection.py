# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 11:09:26 2020

@author: Matador
"""

import cv2
import numpy as np

def preprocess(img):
    
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    filtered = cv2.GaussianBlur(img_gray,(5,5),1)
    edges = cv2.Canny(filtered,190,200)
    
    kernel = np.ones((5,5))
   
    dilated = cv2.dilate(edges, kernel, iterations = 2)
    thers = cv2.erode(dilated, kernel, iterations= 1)
    
    return thers

def getcontours(img,copy):
    
    maxarea = 0
    biggest = np.array([])
    
    contour, hirarchys = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

    for conts in contour:
        area = cv2.contourArea(conts)
        
        if(area >500):
            
            cv2.drawContours(copy,conts,-1,(255,0,0),3)
            peri = cv2.arcLength(conts,True)
            
            k = 0.02
            aprox = cv2.approxPolyDP(conts,k*peri,True)
            
            if(area > maxarea and len(aprox) == 4):
                biggest = aprox
                maxarea = area
                
    return biggest

            
        

cap = cv2.VideoCapture(0)

frameW, frameH = 300,300

size = (frameW,frameH)

cap.set(3,frameW)
cap.set(4,frameH)
cap.set(10,100)

while (True):
    
    success, frame = cap.read()
    frame = cv2.resize(frame,size)
    
    process = preprocess(frame)
    
    copy = frame.copy()
    points = getcontours(process, copy)
    
    if(len(points) == 0):
        print("no encontre nada")
    else:
        print("encontre algo")
    
    cv2.imshow('resultado',process)
    if(cv2.waitKey(1) & 0xFF == ord('q')):
        break