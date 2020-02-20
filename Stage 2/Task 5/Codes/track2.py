"""
    A^4 PROTOCOL Version 1.0

    Tracking Code
"""

import numpy as np
import cv2
import RPi.GPIO as GPIO
import time

##Thippe Setup
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
##Thippe Setup ends

cap = cv2.VideoCapture(1)

redL1 = (150, 80, 80)
redU1 = (180, 255, 255)
redL2 = (0, 100, 100)
redU2 = (10, 255, 255)

cv2.namedWindow("1", cv2.CV_WINDOW_AUTOSIZE)
cv2.namedWindow("2", cv2.CV_WINDOW_AUTOSIZE)

direction = ""

ret, frame = cap.read()
val = cv2.waitKey(30)

x1 = 0
y1 = 0

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
            
            if x - x1 > 5 and y - y1 == 0:
                direction = "South"                                 
                k=0
                r=100
                l=100
                
            elif x1 - x > 5 and y1 - y == 0:
                direction = "North"
                k=1
                r=100
                l=100
                
            elif x - x1 == 0 and y - y1 > 5:
                direction = "East"
                k=1
                r=0
                l=100
                
            elif x - x1 == 0 and y1 - y > 5:
                direction = "West"
                k=1
                r=100
                l=0
                
            elif x - x1 > 5 and y - y1 > 5:
                direction = "South East"
                k=0
                r=100
                l=50

            elif x - x1 > 5 and y1 - y > 5:
                direction = "South West"
                k=0
                r=50
                l=100

            elif x1 - x > 5 and y - y1 > 5:
                direction = "North East"
                k=1
                r=50
                l=100

            elif x1 - x > 5 and y1 - y > 5:
                direction = "North West"
                k=1
                r=100
                l=50 

            else:
                direction = "Nothing"
                r=0
                l=0
                
            if k==1:
                PWMR.ChangeDutyCycle(r)
                PWML.ChangeDutyCycle(l)
                time.sleep(1)
            else :
                PWMR1.ChangeDutyCycle(r)
                PWML1.ChangeDutyCycle(l)
                time.sleep(1)
                
            PWML.ChangeDutyCycle(0)
            PWMR.ChangeDutyCycle(0)
            PWMR1.ChangeDutyCycle(0)
            PWML1.ChangeDutyCycle(0)
            x1 = x
            y1 = y

    print(direction)

    cv2.imshow("1", frame)
    cv2.imshow("2", mask)
    val = cv2.waitKey(30)
    ret, frame = cap.read()

#Thippe stop
PWMR.stop()
PWMR1.stop()
PWML.stop()
PWML1.stop()

GPIO.cleanup()
#Thippe stopped
cv2.destroyAllWindows()
cv2.waitKey(0)
