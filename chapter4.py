# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:21:30 2020

@author: Matador
"""

# colocar figuras, lineas y texto sobre la imagen

import cv2
import os
import numpy as np


img = np.zeros((512,512,3),np.uint8)

# dibujar lineas
color = (200,255,100)

cv2.line(img,(0,0),(300,300),color,3)
cv2.rectangle(img,(0,0),(200,200),color,3)
cv2.line(img,(300,300),(0,512),color,3)
cv2.circle(img,(300,300),50,color,3)

message = "vision artificial"
cv2.putText(img,message,(250,200),cv2.FONT_HERSHEY_COMPLEX,1,color,1)

cv2.imshow("cuadrado",img)