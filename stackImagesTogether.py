import cv2 as cv
import numpy as np
import utilities as ut 

kernel = np.ones((5, 5), np.uint8)
# print(kernel)

path = "resources/image.jpg"
img = cv.imread(path)
img = cv.resize(img, (400, 400))

imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(img, (7, 7), 0)
imgCanny = cv.Canny(img, 100, 200)
imgDilation  = cv.dilate(img, kernel, iterations=2)
imgEroded = cv.erode(img, kernel, iterations=2)

# cv.imshow("Img", img)
# cv.imshow("Greyscale", imgGrey)
# cv.imshow("Blur", imgBlur)
# cv.imshow("Canny", imgCanny)
# cv.imshow("Eroded", imgEroded)

# Stack Images
# stackedImg = ut.stackImages(1, ([img, imgGrey, imgBlur],[img, imgCanny, imgEroded]))
# cv.imshow("Stacked", stackedImg)

frameHeight = 640 
frameWidth = 480

cap = cv.VideoCapture(0)

# cap.set(3, frameWidth) # 3 is default id set for frame Width 
# cap.set(4, frameHeight) # 4 is default id set for frame Height 


while True: 
    success, img = cap.read()
    # cv.imshow("Video", img)
    
    kernel = np.ones((5, 5), np.uint8)
    # print(kernel)

    imgGrey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(img, (7, 7), 0)
    imgCanny = cv.Canny(img, 100, 200)
    imgDilation  = cv.dilate(img, kernel, iterations=2)
    imgEroded = cv.erode(img, kernel, iterations=2)

    stackedImg = ut.stackImages(1, ([img, imgGrey, imgBlur],[img, imgCanny, imgEroded]))
    cv.imshow("Stacked", stackedImg)

    if cv.waitKey(1) & 0xff == ord('q'):
        break;


cv.waitKey(0)
cv.destroyAllWindows()
