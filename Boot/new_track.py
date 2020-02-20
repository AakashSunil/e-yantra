"""
    A^4 PROTOCOL Version 1.0

    Tracking Code
"""

from collections import deque
import numpy as np
import cv2
import time
import RPi.GPIO as GPIO

#Setup Thippe
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

PWMR = GPIO.PWM(24,60)
PWMR1 = GPIO.PWM(23,60)
PWML = GPIO.PWM(17,60)
PWML1 = GPIO.PWM(22,60)

PWMR.start(0)
PWMR1.start(0)
PWML.start(0)
PWML1.start(0)
#Thippe is set up

cap = cv2.VideoCapture(0)

cap.set(3, 320)
cap.set(4, 240)

redL1 = (150, 80, 80)
redU1 = (180, 255, 255)
redL2 = (0, 100, 100)
redU2 = (10, 255, 255)

#cv2.namedWindow("1", cv2.CV_WINDOW_AUTOSIZE)
#cv2.namedWindow("2", cv2.CV_WINDOW_AUTOSIZE)

direction = ""
k=-1
r=0
l=0

ret, frame = cap.read()
val = cv2.waitKey(30)

pts = deque(maxlen = 64)
counter = 0
(dX, dY) = (0, 0)
direction = ""
framecount = 0

print("Started")
while (val != 27):
    if(framecount % 3 == 0):
        #t1 = time.clock()

        #Stop Motors#
        PWMR.ChangeDutyCycle(0)
        PWML.ChangeDutyCycle(0)
        PWMR1.ChangeDutyCycle(0)
        PWML1.ChangeDutyCycle(0)
        
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask1 = cv2.inRange(hsv, np.array(redL1), np.array(redU1))
        mask2 = cv2.inRange(hsv, np.array(redL2), np.array(redU2))
        mask = mask1 | mask2
        mask = cv2.erode(mask, None, iterations = 1)
        mask = cv2.dilate(mask, None, iterations = 1)
    
        cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
        center = None
        
        if len(cnts) > 0:
		    # find the largest contour in the mask, then use
		    # it to compute the minimum enclosing circle and
		    # centroid
            c = max(cnts, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)

            if M["m00"] == 0:
                framecount += 1
                continue

            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
		    # only proceed if the radius meets a minimum size
            if radius > 5:
			    # draw the circle and centroid on the frame,
			    # then update the list of tracked points
                #cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                #cv2.circle(frame, center, 5, (0, 0, 255), -1)
                print("Found", framecount, len(pts))
                pts.appendleft(center)
                """if len(pts) == 32:
                    pts.clear()
                    framecount += 1
                    (dX, dY) = (0, 0)"""
                
        for i in np.arange(1, len(pts)):
	      # if either of the tracked points are None, ignore
		        # them
            if pts[i - 1] is None or pts[i] is None:
                continue
             
		        # check to see if enough points have been accumulated in
		        # the buffer
            if len(pts) >= 2 and i == 1 and pts[-2] is not None:
	        # compute the difference between the x and y
	        # coordinates and re-initialize the direction
	        # text variables
                dX = pts[-2][0] - pts[i][0]
                dY = pts[-2][1] - pts[i][1]
 
                # ensure there is significant movement in the
                # x-direction
            if np.abs(dX) > 5:
                if np.sign(dX) == 1:
                    dirX = "East"
                    l = 0
                    r = 70
                else:
                    dirX = "West"
                    l = 70
                    r = 0
            # ensure there is significant movement in the
            # y-direction
            if np.abs(dY) > 5:
               if np.sign(dY) == 1 : 
                    dirY = "North"
                    if l == 70:
                        r = 70
                        l = 50
                    elif r == 70:
                        l = 70
                        r = 50
                    else:
                        l = r = 70
                    k = 1
               else :
                    dirY = "South"
                    if l == 70:
                        r = 70
                        l = 50
                    elif r == 70:
                        l = 70
                        r = 50
                    else:
                        l = r = 70
                    k = -1

                # handle when both directions are non-empty
            if dirX != "" and dirY != "":
                direction = "{}-{}".format(dirY, dirX)
               # otherwise, only one direction is non-empty
            else:
                direction = dirX if dirX != "" else dirY
                k = 0
        
            if k == 1:
                PWMR.ChangeDutyCycle(r)
                PWML.ChangeDutyCycle(l)
            elif k == -1:
                #PWMR1.ChangeDutyCycle(r)
                #PWML1.ChangeDutyCycle(l)
                PWMR.ChangeDutyCycle(0)
                PWML.ChangeDutyCycle(0)
                PWMR1.ChangeDutyCycle(0)
                PWML1.ChangeDutyCycle(0)
                continue
            else:
                (dirX, dirY) = ("", "")
                PWMR.ChangeDutyCycle(0)
                PWML.ChangeDutyCycle(0)
                PWMR1.ChangeDutyCycle(0)
                PWML1.ChangeDutyCycle(0)

        #t2 = time.clock()
        #print(t2 - t1, framecount)
        #cv2.imshow("1", frame)
        #cv2.imshow("2", mask)
    #print(direction)
    val = cv2.waitKey(15)
    ret, frame = cap.read()
    framecount += 1

cv2.destroyAllWindows()
cv2.waitKey(0)
