import cv2 as cv
import numpy as np

img = cv.imread('/Users/nanda/Documents/OpenCV/IMG_6193.jpeg')
cv.imshow('Original',img)


grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',grey)

#Simple Thresholding 

threshold,thresh = cv.threshold(grey,150,255,cv.THRESH_BINARY)
cv.imshow('Threhsold',thresh)


threshold,thresh_inv = cv.threshold(grey,150,255,cv.THRESH_BINARY_INV)
cv.imshow('Threhsold_INV',thresh_inv)


##Adaptive Thresholding

adaptive_thresh = cv.adaptiveThreshold(grey,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY_INV,13,-1)
cv.imshow('Adaptive Threshold',adaptive_thresh)




cv.waitKey(0)