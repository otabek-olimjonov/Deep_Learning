import cv2
import numpy as np


img = cv2.imread("Photos/self.jpg")
cv2.imshow('Img', img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)


# Laplacian edge detection
lap = cv2.Laplacian(gray, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow('Laplacian Edge', lap)


# Sobel Edge detection
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)
sobel_bitwise = cv2.bitwise_or(sobel_x, sobel_y)

cv2.imshow('Solbel x', sobel_x)
cv2.imshow('Solbel y', sobel_y)
cv2.imshow('Solbel Bitwise', sobel_bitwise)


# Canny edge detection
canny = cv2.Canny(gray, 125, 175)
cv2.imshow("Canny Edge", canny)



cv2.waitKey(0)