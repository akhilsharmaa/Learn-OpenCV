import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow("Blank", blank)

# img = cv.imread("Cats/Cats1.jpg")
# cv.imshow("Cat", img)

# 1. Paint the image a certain color 
blank[:] = 220, 225, 223
# cv.imshow("BLANK", blank)

# 1. Paint the image a certain color 
blank[200:300, 300:400] = 0, 200, 255
# cv.imshow("Green", blank)

# 2. Drow a rectangle 
cv.rectangle(blank, (0, 0), (250, 250),  (20, 255, 230), thickness=3)
# cv.imshow("Rectangle", blank)

# 3. Draw a Circle 
cv.circle(blank, (250, 250), 45,  (0, 0, 230), -1)
# cv.imshow("Circle", blank)

# 4. Draw a Line 
cv.line(blank, (0, 0), (350, 250),  (0, 255, 255), thickness=3)
# cv.imshow("Line", blank)


# 4. Put a Text 
cv.putText(blank, "This is a Text", (225, 225),  cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 255),  thickness=2)
cv.imshow("Line", blank)



cv.waitKey(0)