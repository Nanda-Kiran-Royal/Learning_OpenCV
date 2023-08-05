import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype = 'uint8')

rectangle = cv.rectangle((blank.copy()),(30,30),(370,370),255,-1)
circle = cv.circle((blank.copy()),(200,200),200,255,-1)

cv.imshow("Circle",circle)
cv.imshow("Rectangle",rectangle)
img = cv.imread('IMG_6193.jpeg')
cv.imshow('Original',img)

##bitwise and

bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('Bitwise AND',bitwise_and)
##2.Bit wise OR
bitwise_or = cv.bitwise_or(rectangle,circle)
cv.imshow('Bitwise OR',bitwise_or)

##2.XOR

bitwise_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('XOR',bitwise_xor)

#.NOT
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('NOT',bitwise_not)

cv.waitKey(0)