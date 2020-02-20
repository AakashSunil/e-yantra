"""
    A^4 PROTOCOL Version 1.0

    Tracking Code
"""

import numpy as np
import cv2

cap = cv2.VideoCapture(1)

redL1 = (150, 80, 80)
redU1 = (180, 255, 255)
redL2 = (0, 100, 100)
redU2 = (10, 255, 255)

#cv2.namedWindow("1", cv2.CV_WINDOW_AUTOSIZE)
#cv2.namedWindow("2", cv2.CV_WINDOW_AUTOSIZE)

counter = 0
(dX, dY) = (0, 0)
direction = ""

ret, frame = cap.read()
val = cv2.waitKey(30)

while (val != 27):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask1 = cv2.inRange(hsv, redL1, redU1)
    mask2 = cv2.inRange(hsv, redL2, redU2)
    mask = mask1 | mask2
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations = 2)
    
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    
    if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
		# only proceed if the radius meets a minimum size
        if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
    
    cv2.imshow("1", frame)
    cv2.imshow("2", mask)
    val = cv2.waitKey(30)
    ret, frame = cap.read()

cv2.destroyAllWindows()
cv2.waitKey(0)
