import cv2 as cv;

#? Reading Images
# img = cv.imread('Dogs/dog-puppy-on-garden-royalty-free-image-1586966191.jpg')
# cv.imshow("Dogs", img)
# cv.waitKey(0) 

#? Reading Videos
capture  = cv.VideoCapture("Dogs/DogVideo.mp4")

while True: 
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(24) & 0xFF == ord('d'): 
        break

capture.realease()
cv.destroyAllWindows()
