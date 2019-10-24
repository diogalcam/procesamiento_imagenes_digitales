import cv2 as cv
import numpy as np
import math

#### 1 ####
img = cv.imread("circulos_ruidos.png", 0)
kernel = np.ones((3,3),np.uint8)
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
openingClosing = cv.morphologyEx(closing, cv.MORPH_OPEN, kernel)
cv.imshow("Closing then opening 3x3 kernel",openingClosing)


#### 2 ####
def maskCircle(r):
    mask = np.ones((2*r,2*r),np.uint8)
    for x in range(0,r):
        for y in range(0,r):
            if not(math.sqrt((x - r) ** 2 + (y - r) ** 2) < r):
                mask[x][y] = 0
            if not(math.sqrt((x) ** 2 + (y - r) ** 2) < r):
                mask[x+r][y] = 0
            if not(math.sqrt((x) ** 2 + (y) ** 2) < r):
                mask[x+r][y+r] = 0
            if not(math.sqrt((x - r) ** 2 + y ** 2) < r):
                mask[x][y+r] = 0
    return mask

print(maskCircle(10))

dilation = cv.dilate(openingClosing,maskCircle(15),iterations = 1)
cv.imshow("No círculos negros",dilation)
cv.waitKey(0)


