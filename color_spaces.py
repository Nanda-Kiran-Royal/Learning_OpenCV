## What is color Space ?
## A system representing the an array of color spaces RGB,Grey

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('IMG_6193.jpeg')
cv.imshow('Original Image',img) ## Cv reads a image in BGR format

# plt.imshow(img)
# plt.show()


##BGR to greyscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey Scale Image',gray)


## BGR to HSV Format
hsv = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow('HSV Image',hsv)

## BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('LAB IMage',lab)


# ## BGR to RGB 
# rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
# cv.imshow('RGB',rgb)
# plt.imshow(rgb)
# plt.show()

## HSV to BGR
hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr',hsv_bgr)

## lab_bgr
lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow('LAB_BGR',lab_bgr)

cv.waitKey(0)
