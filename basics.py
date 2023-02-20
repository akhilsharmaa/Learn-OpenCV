import cv2 as cv

img = cv.imread("Cats/Cats1.jpg")
cv.imshow("Cat",  img)

# Converting to grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("BW Cat",  grey)

# Blur Image 
blur = cv.GaussianBlur(img, (9, 9), cv.BORDER_DEFAULT)
# cv.imshow("Blur Cat",  blur)

# EDGE Cascade 
canny = cv.Canny(img, 125, 175)
# cv.imshow("Canny", canny) 

# Dilating the image
dilated = cv.dilate(canny, (7, 7), iterations=3)
# cv.imshow("Dilated", dilated)

# Eroding
eroded = cv.erode(dilated, (7, 7), iterations=3)
# cv.imshow("Eroded", eroded)

# resize 
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_CUBIC)
# cv.imshow("Resized", resized)

# Cropping
cropped = img[100: 200, 200:400]
# cv.imshow("Cropped", cropped)



cv.waitKey(0)
