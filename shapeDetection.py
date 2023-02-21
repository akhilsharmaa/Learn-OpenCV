import cv2 as cv
import numpy as np
import utilities as ut

def getContours(img):
    contours, hierarchy = cv.findContours(img, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    
    for cnt in contours: 
        area = cv.contourArea(cnt)
        
        if area > 500:
        
            perimeter = cv.arcLength(cnt, True)
            approx = cv.approxPolyDP(cnt, 0.02*perimeter, True)
            objCor = len(approx)
            
            ObjType = "None"
            
            if objCor == 3: 
                ObjType = "Triangle"
            elif objCor == 4: 
                ObjType = "Rectangle"
            elif objCor > 4: 
                ObjType = "Circle"
            
            cv.drawContours(imgContour, cnt, -1, (255, 0, 255), thickness=3)
            
            # Draw a Rectangle around all the contours
            x, y, w, h = cv.boundingRect(approx)
            cv.rectangle(imgContour, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            cv.putText(imgContour, ObjType, 
                       (x+(w//2)-10, y+(h//2)-10), cv.FONT_HERSHEY_COMPLEX, 0.5, 
                       (0, 255, 0), 2)
            
            
            # print("Perimeter = ", perimeter, "| Area = ", area, "| Approx = ", len(approx))
            
                
        else: 
            cv.drawContours(imgContour, cnt, -1, (0, 255, 255), thickness=3)
            
            
                 

path = "resources/shapes.png"

img = cv.imread(path)
imgContour = np.zeros_like(img)

imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(img, (7, 7), 1)
imgCanny = cv.Canny(imgBlur, 50, 50)    
imgBlank = np.zeros_like(img)

# Get contours
getContours(imgCanny)

# Stack the Images
imgStack = ut.stackImages(2,[[img, imgGrey, imgBlur], 
                             [imgCanny, imgContour, imgBlank]])

cv.imshow("Stacked Images", imgStack)

cv.waitKey(0)   
