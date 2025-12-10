#!/usr/bin/python3
import cv2
import numpy as np

img_gray=cv2.imread('MyPic.png',cv2.IMREAD_GRAYSCALE)
cv2.imwrite('MyPic_Gray.jpg',img_gray)
window_name='img_gray'
cv2.imshow(window_name, img_gray)
window_name1='reduced Gray Scale'
img_gray_reduced=cv2.imread('MyPic.png',cv2.IMREAD_REDUCED_GRAYSCALE_2)
cv2.imshow(window_name1, img_gray_reduced)

print(bytearray(img_gray_reduced))

# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
