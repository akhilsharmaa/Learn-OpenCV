import cv2 as cv
import numpy as np

faceCascade = cv.CascadeClassifier("resources/haarcascade_frontalface_default.xml")

img = cv.imread("resources/image.jpg")
imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)   

faces = faceCascade.detectMultiScale(imgGrey, 1.1, 4)

for (x, y, w, h) in faces: 
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
cv.imshow("Faces", img)

cv.waitKey(0)