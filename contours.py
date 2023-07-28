import cv2 as cv
import numpy as np


img = cv.imread('IMG_6193.jpeg')
#show image
cv.imshow('Image',img)

##creating a blank image of shape original image
blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank Image',blank)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray Image',gray)
##blur image
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)
##canny image
canny =cv.Canny(blur,125,175)
cv.imshow('Canny Image',canny)
## making a binary image using the thresholding
ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)
##finding the contours
contours, hierarchies = cv.findContours(blur,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(contours))

##drawing the contours
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)

cv.waitKey(0)
