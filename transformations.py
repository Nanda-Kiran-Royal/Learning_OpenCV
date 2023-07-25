import cv2 as cv
import numpy as np

img = cv.imread('/Users/nanda/Documents/OpenCV/IMG_6193.jpeg')
cv.imshow('Original',img)

##1.Translation of image

def imageTranslate(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> left
# -y --> up
# x --> right
# y --> down

translated = imageTranslate(img,-100,100)
cv.imshow('Translated',translated)


##2. Rotation of image
def rotateImage(image,angle,rotPoint=None):
    (height,width) = img.shape[0:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotateImage(img,120,4)
cv.imshow('Rotated',rotated)
cv.waitKey(0)   