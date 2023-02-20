
import cv2 as cv
 
img = cv.imread("blackwidow.jpg")
cv.imshow("Image", img)

#  Color to GREY 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

# Canny Iamges
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)


contours, hierarchies = cv.findContours(canny, cv,)

cv.waitKey(0)