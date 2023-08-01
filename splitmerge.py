import cv2 as cv
import numpy as np

img = cv.imread('IMG_6193.jpeg')
cv.imshow('Original',img)

## 1.Splitting image
blank = np.zeros(img.shape[:2],dtype = 'uint8')
b,g,r = cv.split(img)
blue = cv.merge([b,blank,blank])
red = cv.merge([blank,blank,r])
green = cv.merge([blank,g,blank])




cv.imshow('Blue',blue)
cv.imshow('Green',green)
cv.imshow('Red',red)
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

##2.Merge Image
merged = cv.merge([blue,green,red])
cv.imshow('Merged',merged)
cv.waitKey(0)

