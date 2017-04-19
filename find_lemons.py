import cv2
import numpy as np

img = cv2.imread('lemons.jpeg')
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img1 = cv2.medianBlur(img1,1)
# cv2.imshow("Blur",img1)
# cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles=cv2.HoughCircles(img1,cv2.HOUGH_GRADIENT,1, 30, np.array([]), 80, 20, 3, 50)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    
    cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
    
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,str(circles.shape[1])+' lemons detected',(10,50), font, 0.8,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('detected lemons',img)
cv2.waitKey(0)
cv2.destroyAllWindows()