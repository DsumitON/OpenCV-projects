import numpy as np
import cv2
from scipy import ndimage
"""
kernel_3x3= np.zeros((8,6),order='C', dtype=int)
print(kernel_3x3)
kernel_3x3= np.zeros((3,8),order='F',dtype=float)
print(kernel_3x3)"""
print("\n============== ===============\n")

kernel_3x3 = np.array([[-1, -1, -1],[-1, 8, -1],[-1, -1, -1]])
kernel_5x5 = np.array([[-1, -1, -1, -1, -1],[-1, 1, 2, 1, -1],[-1, 2, 4, 2, -1],[-1, 1, 2, 1, -1],[-1, -1, -1, -1, -1]])
print(kernel_3x3,"\n\n",kernel_5x5)

img = cv2.imread("/mnt/win/Users/Sumit/Documents/SKS_Drive/OPenCV/images/statue_small.jpg",0)
print(img.ndim)
print(img.shape)
"""
noise_img=ndimage.median_filter(img, size=(3,5), footprint=None, output=None, mode='reflect', cval=0.0, origin=0)
blur_oimg=ndimage.gaussian_filter(img, sigma=1, order=0, output=None, mode='constant', cval=0.0, truncate=4.0)
blur_nimg=ndimage.gaussian_filter(noise_img,sigma=0.5)
"""

k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)
blurred = cv2.GaussianBlur(img, (17,17), 0)
g_hpf = img - blurred
#print(img)
cv2.imshow('Image',img)
cv2.imshow("3x3", k3)
cv2.imshow("5x5", k5)
cv2.imshow("blurred", blurred)
cv2.imshow("g_hpf", g_hpf)
"""
cv2.imshow('Median_Image',noise_img)
cv2.imshow('Gaussian_OImage',blur_oimg)
cv2.imshow('Gaussian_Image',blur_nimg)
"""



cv2.waitKey(0)
#cv2.destroyWindow('Image')
cv2.destroyAllWindows()
