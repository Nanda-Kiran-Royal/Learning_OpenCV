import os
import cv2 as cv
import numpy as np

people = []

for i in os.listdir('/Users/nanda/Documents/OpenCV/newwwww'):
    people.append(i)
print(people)
haar_cascade = cv.CascadeClassifier('haar_face.xml')
DIR = '/Users/nanda/Documents/OpenCV/newwwww'
img_ext = ['jpg','png','jpeg','bmp']
import os
import cv2
import imghdr

# # Looping over images
# for img_class in os.listdir(DIR):
#     img_class_dir = os.path.join(DIR, img_class)
    
#     # Skip if the current item is not a directory
#     if not os.path.isdir(img_class_dir):
#         continue
    
#     for image in os.listdir(img_class_dir):
#         image_path = os.path.join(img_class_dir, image)
        
#         try:
#             # Process the image
#             img = cv2.imread(image_path)
            
#             # Check the file extension
#             tip = imghdr.what(image_path)
#             if tip not in img_ext:
#                 print('Image is not in the extension list: {}'.format(image_path))
#                 os.remove(image_path)
#         except Exception as e:
#             print('Image has an issue: {}'.format(image_path))


features =[]
labels = []
def create_train():
    for person in people:
        path = os.path.join(DIR,person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_arry =cv.imread(img_path)
            grey = cv.cvtColor(img_arry,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(grey,1.1,4)

            for (x,y,w,h) in faces_rect:

                faces_roi = grey[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
features = np.array(features,dtype='object')
labels = np.array(labels)
print(f'Lenght of featues list i s {len(features)}')
print(f'Lenght of labels list i s {len(labels)}')

face_recognizer = cv.face.LBPHFaceRecognizer_create()

##Train recognizer on features and labels

face_recognizer.train(features,labels)

face_recognizer.save('face_trained.yml')
##Save trained model to use it later
np.save('features.npy',features) 
np.save('labels.npy',labels) 
