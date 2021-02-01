import cv2

img = cv2.imread('Photos/self.jpg')
cv2.imshow('img', img)

# Averaging Blur
average = cv2.blur(img, (7, 7))
cv2.imshow('Averaging', average)

# Gaussian Blur
gauss = cv2.GaussianBlur(img, (7,7), 0)
cv2.imshow('Gaussian', gauss)

# Median Blur
median = cv2.medianBlur(img, 7)
cv2.imshow('Median', median)

# Bilateral Blur
bilateral = cv2.bilateralFilter(img, 5, 15, 15)
cv2.imshow("Bilateral", bilateral)


cv2.waitKey(0)