import cv2 as cv
import numpy as np

blank_image = np.zeros((500,500,3),dtype ='uint8')
cv.imshow("Blank",blank_image)

# ## 1. Paint image with any color
# blank_image[200:300,400:500] = 0,255,0 
# cv.imshow('Green',blank_image)


## 2. Draw a rectangle
cv.rectangle(blank_image,(0,0),(blank_image.shape[1]//2,blank_image.shape[0]//2), (0,255,0) ,thickness=-1)
cv.imshow('Blank_Image',blank_image)



## 3. Draw a circle
cv.circle(blank_image ,(blank_image.shape[1]//2,blank_image.shape[0]//2),40, (25,100,55) ,thickness=-1)
cv.imshow('Circle',blank_image)


## 4.Draw a Line
cv.line(blank_image,(1,5),(blank_image.shape[1]//2,blank_image.shape[0]//2), (255,100,255) ,thickness=10)
cv.imshow('Line',blank_image)


##5. Adding a image to 
cv.putText(blank_image,'Nandas Mac Book',(10,100),cv.FONT_HERSHEY_SIMPLEX,1.0,(27,32,42),thickness=2)
cv.imshow('Text',blank_image)
cv.waitKey(0)