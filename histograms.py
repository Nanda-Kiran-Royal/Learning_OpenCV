import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('IMG_6193.jpeg')

grey = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gre Image',grey)

# blank = np.zeros(img.shape[:2],dtype = 'uint8')
# circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),500,255,-1)
# mask = cv.bitwise_and(grey,grey,mask=circle)
# cv.imshow('Mask',mask)
# ##Histogram of grey scale
# grey_hist = cv.calcHist([grey],[0],mask,[256],[0,256])


# plt.figure()
# plt.title('Greyscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(grey_hist)
# plt.xlim([0,256])
# plt.show()


## Color Histograms
blank = np.zeros(img.shape[:2],dtype = 'uint8')
mask = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),500,255,-1)
masked = cv.bitwise_and(grey,grey,mask=mask)
cv.imshow('Mask',mask)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')





color = ('b','g','r')
for i,col in enumerate(color):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv.imshow('Original',img)
cv.waitKey(0)