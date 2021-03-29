import cv2

img = cv2.imread('RDJ.jpg')

grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
trained_eye_data = cv2.CascadeClassifier('haarcascade_eye.xml')


face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)
eye_coordinates = trained_eye_data.detectMultiScale(grayscaled_img)


for (x, y, w, h) in face_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)

for (x, y, w, h) in eye_coordinates:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)

cv2.imshow('Face Detector', img)

cv2.waitKey()

print('Code Completed')