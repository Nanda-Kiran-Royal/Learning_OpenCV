import cv2 as cv
import numpy as np


img = cv.imread('/Users/nanda/Documents/OpenCV/IMG_6193.jpeg')
cv.imshow('Original',img)


grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',grey)

#Laplacian 
lap = cv.Laplacian(grey,cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian',lap)



## Sobel Gradients

sobelx = cv.Sobel(grey,cv.CV_64F,1,0)
sobely = cv.Sobel(grey,cv.CV_64F,0,1)

cv.imshow('Sobel X',sobelx)
cv.imshow('Sobel Y',sobely)
combined_sobel = cv.bitwise_or(sobelx,sobely)
cv.imshow('Combined',combined_sobel)

canny = cv.Canny(grey,150,175)
cv.imshow('Canny',canny)
cv.waitKey(0)