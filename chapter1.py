# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 13:58:18 2020

@author: Matador
"""
#leer imagenes, videos y webcam

import cv2
import os

#%% imagenes
folder = 'resources'
file = 'chichiro.jpg'

path = os.path.join(folder,file)
img = cv2.imread(path)

cv2.imshow('Output',img)

#%% videos

filev = 'gimme_love.mp4'
pathv = os.path.join(folder,filev)

cap = cv2.VideoCapture(pathv)

while True:
    
    sucess, img = cap.read()
    cv2.imshow("Video",img)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):
   
        break
    
#%% webcam

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while True:
    
    sucess, img = cap.read()
    cv2.imshow("webcam",img)
    
    if(cv2.waitKey(1) & 0xFF == ord('q')):
   
        break

cv2.VideoCapture(0).release()
