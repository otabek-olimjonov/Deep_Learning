import cv2
import numpy as np

img = cv2.imread('Photos/self.jpg')
cv2.imshow('img', img)


blank = np.zeros(img.shape[:2], dtype='uint8')
cv2.imshow('blank', blank)


mask = cv2.circle(blank, (img.shape[1]//2+120, img.shape[0]//2-90), 150, 255, -1)
cv2.imshow('mask', mask)


masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('masked', masked)


cv2.waitKey(0)