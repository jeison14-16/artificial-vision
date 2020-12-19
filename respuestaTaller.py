# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 22:11:02 2020

@author: JAISSON
"""


import cv2 #OpenCV
import numpy as np


img1 = cv2.imread('image/A.jpg')
I = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
umbral,_ = cv2.threshold(I, 0, 255, cv2.THRESH_OTSU)
mascara = np.uint8((I<umbral)+255)

cv2.imshow("Img COLOR", img1)
pxX = np.size(img1, axis=0)
pxY = np.size(img1, axis=1)
pxXY = np.size(img1, axis=None)

promManual= np.sum(img1) / (pxX * pxY * 3)

suma = np.sum(img1)
minimo = np.min(img1)
maximo = np.max(img1)
prom = np.mean(img1)
var = np.var(img1)
de = np.sqrt(var)

#operaciones avanzadas
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.imshow('::: Image HSV :::', hsv)
I = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow('::: Image GRAY :::', I)

umbral1 = 240
umbral2,_ = cv2.threshold(I, 0, 255, cv2.THRESH_OTSU)
binary = np.uint8((I<umbral2) + 255)
cv2.imshow('::: Image BINARY :::', binary)



cv2.waitKey(0)
cv2.destroyAllWindows