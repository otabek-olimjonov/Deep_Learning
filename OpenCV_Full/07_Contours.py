import cv2
import numpy as np

img = cv2.imread('Photos/self.jpg')
cv2.imshow('img', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
cv2.imshow('gray', gray)

# convert to blur
blur = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_DEFAULT)
cv2.imshow("blur", blur)



# Edge cascade
edge = cv2.Canny(blur, 125, 175)
cv2.imshow("Edge", edge)


#Threshold
ret, thresh = cv2.threshold(gray, 125, 175, cv2.THRESH_BINARY)
cv2.imshow('thresh', thresh)



contours, hierarchies = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
print(len(contours))

cv2.drawContours(blank, contours, -1, (0,255,0), thickness=1)
cv2.imshow("contours", blank)

cv2.waitKey(0)