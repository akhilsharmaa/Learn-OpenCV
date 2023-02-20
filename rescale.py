import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    height = int(frame.shape[0]  * scale)
    width = int(frame.shape[1]  * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Works only for LIVE VIDEO 
    capture.set(3, width)
    capture.set(4, height)
    

#? Reading Videos
capture  = cv.VideoCapture("Dogs/DogVideo.mp4")

while True: 
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, 0.45) 

    # cv.imshow("Video", frame) # original 
    cv.imshow("Video Resized", frame_resized) # resized

    if cv.waitKey(20) & 0xFF == ord('d'): 
        break

capture.realease()
cv.destroyAllWindows()
