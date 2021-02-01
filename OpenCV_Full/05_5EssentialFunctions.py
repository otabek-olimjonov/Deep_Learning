import cv2

img = cv2.imread('Photos/self.jpg')
cv2.imshow("img", img)


# Convert to gray scale img
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray", gray)



# convert to blur
blur = cv2.GaussianBlur(gray, (3,3), cv2.BORDER_DEFAULT)
cv2.imshow("blur", blur)



# Edge cascade
edge = cv2.Canny(blur, 125, 175)
cv2.imshow("Edge", edge)



# Dilating the image
dilated = cv2.dilate(edge, (7,7), iterations=3)
cv2.imshow("dilated", dilated)



# Eroding 
eroded = cv2.erode(dilated, (7,7), iterations=3)
cv2.imshow("eroded", eroded)


# cropping
cropped = img[50:400, 250:600]
cv2.imshow("cropped", cropped)


cv2.waitKey(0)