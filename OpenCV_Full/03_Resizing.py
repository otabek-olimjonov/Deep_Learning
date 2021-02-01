import cv2 #Importing opencv library




###### Create a function to resize ############
def rescaleFrame(frame, scale=0.75): #function to resize
    width = int(frame.shape[1] * scale)  
    height = int(frame.shape[0] * scale)

    dimansions = (width, height)

    return cv2.resize(frame, dimansions, interpolation=cv2.INTER_AREA)





###### Resize Img #######

img = cv2.imread('Photos/self.jpg') #Loading the img from path

resizedimg = rescaleFrame(img) #use the fuction

cv2.imshow('Img', img) #Showing the img with the title of Img

cv2.imshow('resized img', resizedimg) #Showing the resizedimg with the title of resized Img

cv2.waitKey(0) #If you press 0 show method will close




##### Resize Video #####

capture = cv2.VideoCapture('Videos/cat.mp4')  #loading the video from the path

while True: 
    isTrue, frame = capture.read() #Read the Video

    cv2.imshow('video', frame) #show the video

    resizedvideo = rescaleFrame(frame) #use the fuction

    cv2.imshow('resized video', resizedvideo) #show the resized video

    if cv2.waitKey(1) & 0xFF == ord('q'): #if 1 or q pressed, the loop will break
        break


capture.release()
cv2.destroyAllWindows()