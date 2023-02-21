import cv2 as cv
import numpy as np
import utilities

def empty(a):
    pass

path = "resources/YellowMustang.jpeg"

cv.namedWindow("TrackBars")
cv.resizeWindow("TrackBars", 640, 240)

cv.createTrackbar("Hue Min", "TrackBars", 11, 179, empty)
cv.createTrackbar("Hue Max", "TrackBars", 103, 179, empty)

cv.createTrackbar("Sat Min", "TrackBars", 138, 255, empty)
cv.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)

cv.createTrackbar("Val Min", "TrackBars", 55, 255, empty)
cv.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

while True: 
    img = cv.imread(path)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    
    hue_min = cv.getTrackbarPos("Hue Min", "TrackBars")
    hue_max = cv.getTrackbarPos("Hue Max", "TrackBars")
    
    sat_min = cv.getTrackbarPos("Sat Min", "TrackBars")
    sat_max = cv.getTrackbarPos("Sat Max", "TrackBars")
    
    val_min = cv.getTrackbarPos("Val Min", "TrackBars")
    val_max = cv.getTrackbarPos("Val Max", "TrackBars")
    
    print(hue_min, hue_max, sat_min, sat_max, val_min, val_max)
    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])
    
    
    mask = cv.inRange(imgHSV, lower, upper)
    imgResult = cv.bitwise_and(img, img, mask=mask)

    # cv.imshow("Original", img)
    # cv.imshow("HSV", imgHSV)
    # cv.imshow("Mask", mask)
    # cv.imshow("Mask", imgResult)
    
    stackedImg = utilities.stackImages(1,[[img, imgHSV], [mask, imgResult]])
    cv.imshow("Result", stackedImg)
    
    cv.waitKey(1)

# mustang detected : 11 103 138 255 55 255