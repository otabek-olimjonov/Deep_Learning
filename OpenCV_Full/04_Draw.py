import cv2
import numpy as np # importing numpy library

blank = np.zeros((600,600,3), dtype='uint8') # to create blank img
cv2.imshow("blank", blank) 

# # 1.Color the frame
# blank[:] = 0,255,0
# cv2.imshow('Green', blank)



# # 2.rectangle Function is to draw a rectangle (Name, (Beginning points), (Ending Points), thickness) if thickness = -1, the frame filled 
# cv2.rectangle(blank, (200,200), (400,400), (0,255,0), thickness=2)
# cv2.imshow("rectangle", blank)



# # 3.Circle Function is to draw a circle (name, Center, radius, color, thinkness)
# cv2.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 200, (0,255,0), thickness=-1)
# cv2.imshow("Circle", blank) 



# # 4.Line function is to draw a line (name, beginning point, ending point, color, thinkness)
# cv2.line(blank, (200,200), (400,400), (0,255,0), thickness=3)
# cv2.imshow("line", blank)



# 5.putText Function is to put the text on the frame (name, text, Beginning point, Font, scale, color, thinkness) 
cv2.putText(blank, "Learn the code", (170,300), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0,255,0), 2)
cv2.imshow("PutText", blank)

cv2.waitKey(0)