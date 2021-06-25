import cv2
import numpy as np


webcam = cv2.VideoCapture("http://10.0.0.3:8080/video")

while(1):

    _, imageFrame = webcam.read()

    cv2.imshow("Hopefully a webcam ^^", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
