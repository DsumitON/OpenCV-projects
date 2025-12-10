import cv2
import numpy as np

# Read image as color
img = cv2.imread(r"/mnt/win/Users/Sumit/Documents/SKS_Drive/OPenCV/images/bottle_sks.jpeg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold (binary image)
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_NONE)
print(contours)
# Make a copy of original for drawing
color = img.copy()

# Draw all contours in green
cv2.drawContours(color, contours, -1, (0,255,0), 2)

# Display
cv2.imshow("Original", img)
cv2.imshow("Threshold", thresh)
print(ret)
cv2.imshow("Contours", color)

cv2.waitKey(0)
cv2.destroyAllWindows()

