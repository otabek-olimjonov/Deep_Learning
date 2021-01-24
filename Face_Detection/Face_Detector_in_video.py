import cv2
import numpy as np

cap = cv2.VideoCapture(0)


trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')




while(True):

    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480)) 


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_coordinates = trained_face_data.detectMultiScale(gray)

    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)

    


    cv2.imshow('Face Detector',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
