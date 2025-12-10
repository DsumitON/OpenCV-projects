#!/usr7bin/python3
import cv2

img=cv2.imread('MyPic.png')
img[150,120][0]=255
img[150,120][1]=0
img[150,120][2]=0
#img[150,120] = [255,0,0]
print('Pixel value is ',img.item(150,120,0))

print('Pixel value is ',img.item(150,120,1))

print('Pixel value is ',img.item(150,120,2))
img = cv2.imread('MyPic.png')
img[:, :, 1] = 0
img[:, :, 0] = 255
print('Pixel value is ',img.item(150,120,0))

print('Pixel value is ',img.item(150,120,1))

print('Pixel value is ',img.item(150,120,2))
cv2.imwrite('Modified_white_image.png',img)


img = cv2.imread('MyPic.png')
my_roi = img[0:100, 0:100]
img[300:400, 300:400] = my_roi
cv2.imwrite('Modified_white_image.png',img)
