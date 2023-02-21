import cv2 as cv
import numpy as np

# Face Cascade Model
faceCascade = cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

cap = cv.VideoCapture(0)

while True: 
    success, img = cap.read()
    imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   
    faces = faceCascade.detectMultiScale(imgGrey, 1.1, 4)
    
    for (x, y, w, h) in faces: 
        cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 3)
    
    cv.imshow("Faces", img)

    if cv.waitKey(50) & 0xff == ord('q'):
        break;

cv.destroyAllWindows()