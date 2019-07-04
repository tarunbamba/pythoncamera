# to use cv2 please install perform the command pip install opencv-python
import cv2
capture = cv2.VideoCapture(0)
while(True):
    ret, frame = capture.read()
#imshow used display an image in a window. The window automatically fits to the image size
    cv2.imshow('video', frame)
# 27 is ASCII value of ESC key
#  function which displays the image for specified milliseconds  
  if cv2.waitKey(1) == 27:  
        break
