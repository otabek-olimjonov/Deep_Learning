import cv2
import numpy as np


img = cv2.imread("Photos/self.jpg")
cv2.imshow('img', img)

# blank img
blank = np.zeros(img.shape[:2], dtype='uint8')

# split RGB into 3 channels
b, g, r = cv2.split(img)

# Show all 3 Channels
cv2.imshow('blue', b)
cv2.imshow('green', g)
cv2.imshow('red', r)

# Merge 3 Channels togather
merged = cv2.merge([b,g,r])
cv2.imshow('merged', merged)

# Single channels
blue = cv2.merge([b,blank,blank])
green = cv2.merge([blank,g,blank])
red = cv2.merge([blank,blank,r])

# Show them
cv2.imshow('blue', blue)
cv2.imshow('green', green)
cv2.imshow('red', red)


cv2.waitKey(0)