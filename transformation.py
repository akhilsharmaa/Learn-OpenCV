import cv2 as cv
import numpy as np

# img = cv.imread("Cats/4e5583748bc4000805df50e4ebcafffc.png")
img = cv.imread("blackwidow.jpg")
cv.imshow("Image", img)

# Translation 
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left 
# -y --> UP
# x ---> Right 
# y ---> Down 

translated = translate(img, 100, 100);
# cv.imshow("Translated", translated)


# Rotate 
def rotate(img, angle, rotPoint=None):
    height, width = img.shape[:2]
    
    if rotPoint == None : 
        rotPoint = width//2, height//2
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions =  width, height;
    
    return cv.warpAffine(img, rotMat, dimensions)   

rotated = rotate(img, 45) 
# cv.imshow("Rotated", rotated)

# Resize 
resized = cv.resize(img, (400, 400), interpolation=cv.INTER_CUBIC)
# cv.imshow("Resized", resized)


# Flipping
flip = cv.flip(img, -1)
# cv.imshow("Resized", flip)


# Cropping 
cropped = img[100:400,  300:600]
cv.imshow("Cropped", cropped)


cv.waitKey(0)
cv.destroyAllWindows()