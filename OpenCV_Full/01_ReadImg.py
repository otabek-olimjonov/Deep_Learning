import cv2 #Importing opencv library

img = cv2.imread('Photos/self.jpg') #Loading the img from path

cv2.imshow('Img', img) #Showing the img with the title of Img

cv2.waitKey(0) #If you press 0 show method will close