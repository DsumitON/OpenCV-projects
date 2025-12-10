#!/usr/bin/python3
import numpy
import cv2
from scipy import ndimage


#read image
img=cv2.imread(r"/mnt/win/Users/Sumit/Documents/SKS_Drive/OPenCV/images/pumkin.png")
#img=cv2.imread(r"/home/sksuser/Pictures/ros2_image.png")

cv2.imshow('Original',img)

img_blr=ndimage.median_filter(img, size=(3,5,1), footprint=None, mode='reflect')
blurredSrc = cv2.medianBlur(img, 7)
img_gray=cv2.cvtColor(blurredSrc, cv2.COLOR_BGR2GRAY)
graySrc=cv2.Laplacian(img_gray, cv2.CV_8U, ksize = 5)
edge = cv2.Canny(img, 100, 200, apertureSize=5)



'''
cv2.imshow('BlurImage_NDIMAGE',img_blr)
cv2.imshow('BlurImage_CV2',blurredSrc)
cv2.imshow('GRAYImage_CV2',img_gray)
cv2.imshow('EDGEImage_CV2',graySrc)'''
cv2.imshow('Cannyedge', edge)


cv2.waitKey(0)
cv2.destroyAllWindows()

