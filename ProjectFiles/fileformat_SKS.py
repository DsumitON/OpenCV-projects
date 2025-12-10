#!/usr/bin/python3
import numpy
import cv2

image=cv2.imread('MyPic.png')
im1=cv2.imread('MyPic.png',cv2.IMREAD_GRAYSCALE)
print(image)
print(im1)
cv2.imwrite('MyPic.jpg',im1)
