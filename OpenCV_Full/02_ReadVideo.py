import cv2 #Importing opencv library

capture = cv2.VideoCapture('Videos/cat.mp4')  #loading the video from the path

while True: 
    isTrue, frame = capture.read() #Read the Video

    cv2.imshow('video', frame) #show the video

    if cv2.waitKey(1) & 0xFF == ord('q'): #if 1 or q pressed, the loop will break
        break


capture.release()
cv2.destroyAllWindows()