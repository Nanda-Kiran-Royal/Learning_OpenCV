import cv2 as cv
import numpy as np

img = cv.imread('/Users/nanda/Desktop/63e0f74e-fb1d-4887-8cc6-829f5b05adb4.jpg')
cv.imshow('Original',img)

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Grey',grey)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect= haar_cascade.detectMultiScale(grey,1.1,3)
print(f'Number of faces found = {len(faces_rect)}')
for (x,y,w,h) in faces_rect:
    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow('Detected Faces',img)
cv.waitKey(0)