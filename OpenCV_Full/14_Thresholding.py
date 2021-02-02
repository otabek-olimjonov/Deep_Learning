import cv2
import numpy as np


img = cv2.imread("Photos/self.jpg")
cv2.imshow('Img', img)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)


threshold, thresh = cv2.threshold(gray, 125, 256, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh)


threshold, thresh_inv = cv2.threshold(gray, 125, 256, cv2.THRESH_BINARY_INV)
cv2.imshow('thresh inv', thresh_inv)


adaptive_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 9)
cv2.imshow('Adaptive thresh', adaptive_thresh)


cv2.waitKey(0)