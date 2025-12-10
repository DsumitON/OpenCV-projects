#!/usr/bin/python3
import numpy
import cv2

img=numpy.zeros((3,3),dtype=numpy.uint8)
print(img)

print(type(img))

print('\n============================\n')
img = numpy.zeros((5, 3), dtype=numpy.uint8)

img= cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
print(img.shape)
print(img)
