# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 15:04:04 2020

@author: Matador
"""

# recortar y hacer resizes sobre imagenes


import cv2
import os

folder = 'resources'
file = 'chichiro.jpg'
path = os.path.join(folder,file)

img = cv2.imread(path)

#%%

print(img.shape)

# cambiar tmaño de la imagen
imgrs = cv2.resize(img,(400,200))

cv2.imshow("imagen",img)
cv2.imshow("resize",imgrs)

# recortar la imagen

imgc = img[0:800,200:300]
cv2.imshow("recortada",imgc)

