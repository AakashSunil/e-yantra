import threading
import time
import socket
import numpy as np
import cv2
#import RPi.GPIO as GPIO


k = 0
r = 0
l = 0

def marker():
    """
        colors
    """
    return

def comm():
    print "Started Communcation Thread"   
    
    UDP_IP_R = "192.168.43.128"
    UDP_PORT_R = 5005
    
    UDP_IP_S = "192.168.43.1"
    UDP_PORT_S = 4210

    sock_r = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    
    sock_r.bind((UDP_IP_R, UDP_PORT_R))

    sock_s = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    
    data, addr = sock_r.recvfrom(1024)

    while True:
        if len(data) > 0:
            """
                1 = checkpoint
                2 = left
                3 = right
                4 = reverse
            """
            MESSAGE = "%s recieved" %data
            
            sock_s.sendto(MESSAGE, (UDP_IP_S, UDP_PORT_S))

            if data == '1':
                color = marker()
                sock_s.sendto(color, (UDP_IP_S, UDP_PORT_S))

        data, addr = sock_r.recvfrom(1024) # buffer size is 1024 bytes
        print "received message:", data
    
    return

def track(e):
    print "Started Tracker Thread"

    global k
    global l
    global r

    cap = cv2.VideoCapture(0)
    
    cap.set(3, 320)
    cap.set(4, 240)

    cv2.namedWindow("1", cv2.CV_WINDOW_AUTOSIZE)

    redL1 = (150, 80, 80)
    redU1 = (180, 255, 255)
    redL2 = (0, 100, 100)
    redU2 = (10, 255, 255)

    ret, frame = cap.read()
    val = cv2.waitKey(10)

    (dX, dY) = (0, 0)
    x1 = y1 = 0

    while (cv2.waitKey(40) != 27):
        e.clear()
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
            c = max(cnts, key = cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)

            if M["m00"] == 0:
                M["m00"] = 1

            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
		    # only proceed if the radius meets a minimum size
            if radius > 5:
			    # draw the circle and centroid on the frame,
			    # then update the list of tracked points
                cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 0, 255), -1)
                (x, y) = center

                dX = x1 - x
                dY = y1 - y

                x1 = x
                y1 = y
                
                if np.abs(dX) > 2:
                    if np.sign(dX) == 1:
                        # "East"
                        l = 0
                        r = 100
                    else:
                        # "West"
                        l = 100
                        r = 0
                # ensure there is significant movement in the
                # y-direction
                elif np.abs(dY) > 2:
                    if np.sign(dY) == 1 : 
                        # "North"
                        if l == 100:
                            r = 100
                            l = 80
                        elif r == 100:
                            l = 100
                            r = 80
                        else:
                            l = r = 100
                        k = 1
                    else :
                        # "South"
                        if l == 100:
                            r = 100
                            l = 80
                        elif r == 100:
                            l = 100
                            r = 80
                        else:
                            l = r = 100
                        k = -1
                else:
                    k = 0

                print ("In Track ", k , l, r)
                e.set()
            
            else:
                k = 0
     
        cv2.imshow("1", frame)
        ret, frame = cap.read()
    k = l = r = 0
    return 

def mv_motor(e):
    
    print "Started Motor Thread"
    
    global k
    global l
    global r

    #Setup Thippe
    """GPIO.setmode(GPIO.BCM)
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
    PWML1.start(0)"""

    while True:
   
        while not e.isSet():
            e.wait()

        print ("In Motor ", k , l, r)

        if k == 0:
            """PWMR.ChangeDutyCycle(0)
            PWML.ChangeDutyCycle(0)
            PWMR1.ChangeDutyCycle(0)
            PWML1.ChangeDutyCycle(0)"""
        
        if k == 1:
            """PWMR.ChangeDutyCycle(r)
            PWML.ChangeDutyCycle(l)"""
        
        if k == -1:
            """PWMR1.ChangeDutyCycle(r)
            PWML1.ChangeDutyCycle(l)"""
    return

mv_event = threading.Event()

communication = threading.Thread(name = 'comm', target = comm)
tracker = threading.Thread(name = 'tracker', target = track, args=(mv_event,))

motor = threading.Thread(name = 'motor', target = mv_motor, args=(mv_event,))

communication.start()
time.sleep(5)

tracker.start()
time.sleep(1)

motor.start()