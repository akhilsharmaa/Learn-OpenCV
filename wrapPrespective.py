import cv2 as cv
import numpy as np

img = cv.imread("resources/card.jpg")
cv.imshow("Image", img) 

width, height = 250, 350

#                           TOP-RIGHT   TOP-LEFT   DOWN-LEFT    DOWN-RIGHT 
sourceCorners = np.float32([[344, 79], [548, 106], [291, 313], [514, 343]])
destinationCorners = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv.getPerspectiveTransform(sourceCorners, destinationCorners)
imgOutput = cv.warpPerspective(img, matrix, (width, height))

cv.imshow("Wraped Image", imgOutput)

cv.waitKey(0)