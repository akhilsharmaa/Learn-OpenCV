import cv2 as cv

frameHeight = 640 
frameWidth = 480

cap = cv.VideoCapture(0)
# cap = cv.VideoCapture(1) # when Web-cam is connect 

cap.set(3, frameWidth) # 3 is default id set for frame Width 
cap.set(4, frameHeight) # 4 is default id set for frame Height 


while True: 
    success, img = cap.read()
    cv.imshow("Video", img)
    
    if cv.waitKey(1) & 0xff == ord('q'):
        break;

cv.destroyAllWindows()