import cv2 as cv
#  # Reading the images in open CV
img = cv.imread('/Users/nanda/Documents/OpenCV/voice-capture.jpg')
cv.imshow('Adidas', img)
# cv.waitKey(0)


# reading the videos in OpenCV



#Resizing the video and image Of existing video

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)


#Function for changing the resolution of live image or video

def changeRes(width,height):
    # Live video
    capture.set(3,width)
    capture.set(4,height)

resized_image = rescaleFrame(img,scale = 0.5)
cv.imshow('rescaled_image',resized_image)

capture = cv.VideoCapture('/Users/nanda/Documents/OpenCV/goju3.mp4') ##------> if we give file path it reads the file or if we give 0 it reads from web cam

while True:
    isTrue,frame = capture.read()
    frame_resized = rescaleFrame(frame,scale=.99)
    
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()


