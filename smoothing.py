import cv2 as cv
import numpy as np
img = cv.imread('IMG_6193.jpeg')
cv.imshow('Original',img)

##1.Averaging
average = cv.blur(img,(7,7))
cv.imshow('Blur',average)

##2.Gaussian Blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('Gaussian Blur',gauss)

##3.Median Blur
median = cv.medianBlur(img,3)
cv.imshow('Medain Blur',median)

##4.Bilateral Blur
bilateral = cv.bilateralFilter(img,5,15,15)
cv.imshow('Bilateral Blur',bilateral)
cv.waitKey(0)