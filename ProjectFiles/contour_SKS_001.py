#!/usr/bin/python3

import numpy
import cv2

# read an Image
img=cv2.imread("/mnt/win/Users/Sumit/Documents/SKS_Drive/OPenCV/images/SKS_Mint.jpeg")

#convert to gray
img_gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# convert gray to black and white (Binary Image)- as contour only work on Binary Image i.e black and white picture. 
ret,img_black = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# Find contours lines
contours, hierarchy = cv2.findContours(img_black, cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Length of contours: ",len(contours))

#copy Image where contour to be applied
img_copy=img.copy()

#add contour to copy image and Draw all contours in green(0,255,0)

cv2.drawContours(img_copy, contours, -1, (0,255,0), 2)

'''
cv2.drawContours(imagecopy, contours, index of contours,BGR color,Line thickness = 2 pixels)
 
#imagecopy - This is the image where contours will be drawn. - You should always create a copy of the original image so you don’t overwrite 
#contours - This is the list of contours returned by:contours, hierarchy = cv2.findContours(...)-Each contour is a list of (x, y) points.
#index of contours - it is the index of the contour you want to draw. 0 → first contour,1 → second contour,..etc, -1 → ALL contour that means OpenCV will iterate through every contour in the contours list.
# BGR color - here its green hence (0,255,0)
#Line thickness = 2 pixels
'''


cv2.imshow('original',img)
cv2.imshow('gray Image',img_gray)
cv2.imshow('Black and white Image',img_black)
cv2.imshow('Contour Image',img_copy)

cv2.waitKey(0)
cv2.destroyAllWindows()
