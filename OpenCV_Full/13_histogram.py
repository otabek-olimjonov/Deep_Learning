import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread('Photos/self.jpg')
cv2.imshow('img', img)


blank = np.zeros(img.shape[:2], dtype='uint8')


# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray)


# circle = cv2.circle(blank, (img.shape[1]//2+120, img.shape[0]//2-90), 150, 255, -1)
# cv2.imshow('circle', circle)


# mask = cv2.bitwise_and(gray, gray, mask=circle)
# cv2.imshow('mask', mask)


# gray_hist = cv2.calcHist([gray], [0], mask, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()


# Color Histogram
mask = cv2.circle(blank, (img.shape[1]//2+120, img.shape[0]//2-90), 150, 255, -1)


masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow('mask', masked)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv2.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()


cv2.waitKey(0)