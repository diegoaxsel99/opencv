# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 14:37:55 2020

@author: Matador
"""
#operaciones basicas 

import cv2
import os
import numpy as np

folder = 'resources'
file = 'chichiro.jpg'
path = os.path.join(folder,file)

img = cv2.imread(path)

#%% operaciones sobre las imagenes

# mostrar gris
img_gris = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("imagen en gris",img_gris)
 
#filtrado

img_Blur = cv2.GaussianBlur(img_gris,(7,7),0)

cv2.imshow("imagen filtrada",img_Blur)

#los bordes de una imagen

imgCanny = cv2.Canny(img,100,200)

cv2.imshow("bordes",imgCanny)

# dilatar los bordes de la imagen

kernel = np.ones((2,2),np.uint8)
imgd = cv2.dilate(imgCanny,kernel,iterations = 1)

cv2.imshow("dilatada",imgd)
