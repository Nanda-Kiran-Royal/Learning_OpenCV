## Converting image to gray scale

import cv2 as cv
import numpy as np

img = cv.imread('/Users/nanda/Documents/OpenCV/IMG_6193.jpeg')
cv.imshow('IMG',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',gray)


## 2 . blurring an image using gaussian blur
blur = cv.GaussianBlur(img,(31,31),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

'''#//What is the max kernel size in cv.GaussianBlur?
The error message is saying that the kernel width 
and height must be odd numbers. This is because the Gaussian blur
 kernel is a 2D array, and the convolution operation requires that the kernel 
 be an odd number of pixels wide and tall. If the kernel is an even number of 
 pixels wide or tall, then the convolution operation will not work correctly.'''

##3. Edge cascade
canny = cv.Canny(img,125,175)
cv.imshow('Canny',canny)

## 4. Dialating the image
dialated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dialated',dialated)

##5.Erroded
erroded = cv.erode(dialated,(9,9),iterations=3)
cv.imshow('Erroded',erroded)

##6.Resize and crop images
resized =cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)
# resized =cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized2',resized)
# resized =cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
# cv.imshow('Resized3',resized)

## 7.cropping
cropped = img[50:200,20:400]
cv.imshow('Cropped',cropped)
# //how to crop image in ?
height, width = img.shape[:2]
print(height,width)
cv.waitKey(0)
