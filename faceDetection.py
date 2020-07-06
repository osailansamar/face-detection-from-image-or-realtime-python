#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import required libraries
import cv2
import sys


# In[ ]:


#user supplied values
cascPath = "haarcascade_frontalface_default.xml"

#create haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

#scan picture
image = cv2.imread("faces3.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#recognize faces
faces = faceCascade.detectMultiScale(sgray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
print("There is {0} faces in the picture.".format(len(faces)))

#surround detected faces with a rectangle
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Detected faces", image)
cv2.waitKey(0)


# In[ ]:


cap = cv2.VideoCapture(0)
while(True):
    
    #detect faces in a live camera frame-by-frame
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #recognize faces
    faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    print("There is {0} faces in the picture.".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    #display result
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


# In[ ]:




