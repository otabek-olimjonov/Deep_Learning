import cv2
import matplotlib.pyplot as plt


img = cv2.imread("Photos/self.jpg")
cv2.imshow('img', img)


# RGB to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)


# RGB to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)


# BGR to LAB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('Lab', lab)


# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('rgb', rgb)

# BGR to RGB using matplotlib
plt.imshow(img)
plt.show()

# RGB to BGR using matplotlib
plt.imshow(rgb)
plt.show()