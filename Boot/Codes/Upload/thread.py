import threading
import time
import socket
import numpy as np
import cv2
import RPi.GPIO as GPIO


k = 0
r = 0
l = 0
rev = 0
left = 0
right = 0
m = 0

capture = cv2.VideoCapture(0)
ret, temp = capture.read()
cv2.waitKey(30)
capture.release()

def marker():
    """
        colors
        91 - Red
        92 - Green
        93 - Blue
        94 - Sky Blue
        95 - Pink
        96- Yellow
        97 - While
    """
    global temp
    dim = temp.shape
    # red marker         
    red_low_bound0 = np.array([175, 100, 100])
    red_up_bound0 = np.array([180, 255, 255])
    red_low_bound1 = np.array([0, 100, 100])
    red_up_bound1 = np.array([10, 255, 255])

    red_mask1 = cv2.inRange(temp, red_low_bound0, red_up_bound0)
    red_mask2 = cv2.inRange(temp, red_low_bound1, red_up_bound1)
    red_mask = red_mask1 | red_mask2

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if red_mask[i,j] > 127:
                return 'R' #Red
    
    # green marker
    green_low_bound = np.array([50, 100, 100])
    green_up_bound = np.array([70, 255, 255])
    
    green_mask = cv2.inRange(temp, green_low_bound, green_up_bound)

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if green_mask[i,j] > 127:
                return 'G' #Green
            
    # blue marker
    blue_low_bound = np.array([130, 100, 100])
    blue_up_bound = np.array([150, 255, 255])

    blue_mask = cv2.inRange(temp, blue_low_bound, blue_up_bound)

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if blue_mask[i,j]>127:
                return 'B' #Blue
            
    # sky blue marker
    sblue_low_bound = np.array([90, 100, 100])
    sblue_up_bound = np.array([120, 255, 255])

    sblue_mask = cv2.inRange(temp, sblue_low_bound, sblue_up_bound)

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if sblue_mask[i,j]>127:
                return 'S' #Sky Blue

    # pink marker
    pink_low_bound = np.array([145, 100, 100])
    pink_up_bound = np.array([170, 255, 255])
    
    pink_mask = cv2.inRange(temp, pink_low_bound, pink_up_bound)

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if pink_mask[i,j]>127:
                return 'P' #Pink
            
            
    # yellow marker
    yellow_low_bound = np.array([25, 100, 100])
    yellow_up_bound = np.array([35, 255, 255])
    
    yellow_mask = cv2.inRange(temp, yellow_low_bound, yellow_up_bound)

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if yellow_mask[i,j]>127:
                return 'Y' #Yellow
    return 'W' 

def comm(e):
    print "Started Communcation Thread"   

    global k
    global rev
    global left
    global right
    global m
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(13,GPIO.OUT) #33
    GPIO.setup(19,GPIO.OUT) #35
    GPIO.setup(26,GPIO.OUT) #37

    GPIO.output(13,GPIO.HIGH)
    GPIO.output(19,GPIO.HIGH)
    GPIO.output(26,GPIO.HIGH)

    UDP_IP_R = "192.168.10.1"
    UDP_PORT_R = 5005
    
    UDP_IP_S = "192.168.10.27"
    UDP_PORT_S = 4210

    sock_r = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    
    sock_r.bind((UDP_IP_R, UDP_PORT_R))

    sock_s = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    
    data, addr = sock_r.recvfrom(1024)

    while True:
        data, addr = sock_r.recvfrom(1024) # buffer size is 1024 bytes
        print "received message:", data
        if len(data) > 0:
            """
                1 = checkpoint + turn on LED
                2 = left
                3 = right
                4 = reverse
                5 = turn off LED
            """
            #MESSAGE = "%s recieved" %data
            k = -2
            e.set()
            #sock_s.sendto(MESSAGE, (UDP_IP_S, UDP_PORT_S))

            if data == '1':
                color = marker()
                print color
                sock_s.sendto(str(color), (UDP_IP_S, UDP_PORT_S))
                if color == 'W':
                    GPIO.output(13,GPIO.LOW)
                    GPIO.output(19,GPIO.LOW)
                    GPIO.output(26,GPIO.LOW)
                elif color == 'Y':
                    GPIO.output(13,GPIO.LOW)
                    GPIO.output(19,GPIO.LOW)
                    GPIO.output(26,GPIO.HIGH)
                elif color == 'P':
                    GPIO.output(13,GPIO.LOW)
                    GPIO.output(19,GPIO.HIGH)
                    GPIO.output(26,GPIO.LOW)

                elif color == 'S':
                    GPIO.output(13,GPIO.HIGH)
                    GPIO.output(19,GPIO.LOW)
                    GPIO.output(26,GPIO.LOW)

                elif color == 'B':
                    GPIO.output(13,GPIO.HIGH)
                    GPIO.output(19,GPIO.HIGH)
                    GPIO.output(26,GPIO.LOW)

                elif color == 'G':
                    GPIO.output(13,GPIO.HIGH)
                    GPIO.output(19,GPIO.LOW)
                    GPIO.output(26,GPIO.HIGH)

                else: #R
                    GPIO.output(13,GPIO.LOW)
                    GPIO.output(19,GPIO.HIGH)
                    GPIO.output(26,GPIO.HIGH)

            if data == '6':
                rev = 1
                time.sleep(1)
                MESSAGE = '0'
                sock_s.sendto(MESSAGE, (UDP_IP_S, UDP_PORT_S))
                print "rev successful"
                    
            if data == '5':
                GPIO.output(13,GPIO.HIGH)
                GPIO.output(19,GPIO.HIGH)
                GPIO.output(26,GPIO.HIGH)

            if data == '3':
                left = 1
                if m == 0:
                    time.sleep(2.3)
                else:
                    time.sleep(1)
                MESSAGE = '1'
                sock_s.sendto(MESSAGE, (UDP_IP_S, UDP_PORT_S))
                print "left done"
                
            if data == '2':
                right = 1
                if m == 0:
                    time.sleep(2.3)
                else:
                    time.sleep(1)
                MESSAGE = '1'
                sock_s.sendto(MESSAGE, (UDP_IP_S, UDP_PORT_S))
                print "right done"
                
            k = 0
            e.set()
    return

def track(e):

    global k
    global l
    global r
    global temp
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 320)
    cap.set(4, 240)

    #cv2.namedWindow("1", cv2.CV_WINDOW_AUTOSIZE)

    redL1 = (140, 80, 80)
    redU1 = (180, 255, 255)
    redL2 = (0, 100, 100)
    redU2 = (10, 255, 255)

    ret, frame = cap.read()
    val = cv2.waitKey(10)

    (dX, dY) = (0, 0)
    
    e.set()
    print "Started Tracker Thread"
    
    while (cv2.waitKey(30) != 27):
        if k == -2:
            continue
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        temp = hsv
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
                ret, frame = cap.read()
                continue

            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
		    # only proceed if the radius meets a minimum size
            if radius > 2:
			    # draw the circle and centroid on the frame,
			    # then update the list of tracked points
                #cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                #cv2.circle(frame, center, 5, (0, 0, 255), -1)
                (x, y) = center

                dX = x - 160
                dY = 120 - y
                    
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
                if np.abs(dY) > 2:
                    if np.sign(dY) == 1 : 
                        # "North"
                        if l == 100:
                            r = 80
                            l = 100
                        elif r == 100:
                            l = 80
                            r = 100
                        else:
                            l = r = 100
                        k = 1
                    else :
                        # "South"
                        if l == 100:
                            r = 80
                            l = 100
                        elif r == 100:
                            l = 80
                            r = 100
                        else:
                            l = r = 100
                        k = -1

                #print ("In Track ", k , l, r)
            
            else:
                k = l = r = 0
        else:
            k = l = r = 0
        e.set()
        ret, frame = cap.read()
    k = l = r = 0
    return 

def mv_motor(e):
    e.clear()
    
    global k
    global l
    global r
    global rev
    global left
    global right
    global m
    
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

    while not e.isSet():
        e.wait()

    print "Started Motor Thread"
    
    while True:
        e.clear()
        while not e.isSet():
            e.wait()
        
        #print ("In Motor ", k , l, r)

        if k == 0 or k == -2:
            PWMR.ChangeDutyCycle(0)
            PWML.ChangeDutyCycle(0)
            PWMR1.ChangeDutyCycle(0)
            PWML1.ChangeDutyCycle(0)
        
        if k == 1:
            PWMR.ChangeDutyCycle(r)
            PWML.ChangeDutyCycle(l)
        
        if k == -1:
            """PWMR.ChangeDutyCycle(0)
            PWML.ChangeDutyCycle(0)
            PWMR1.ChangeDutyCycle(0)
            PWML1.ChangeDutyCycle(0)"""

        if rev == 1:
            rev = 0
            PWMR.ChangeDutyCycle(100)
            PWML1.ChangeDutyCycle(100)
            time.sleep(1.5)
            PWMR.ChangeDutyCycle(0)
            PWML1.ChangeDutyCycle(0)
                
        if left == 1:
            left = 0
            PWMR1.ChangeDutyCycle(100)
            PWML.ChangeDutyCycle(100)
            time.sleep(.75)
            PWMR1.ChangeDutyCycle(0)
            PWML.ChangeDutyCycle(0)
            time.sleep(0.01)
            if m == 0:
                m = 1
                PWMR.ChangeDutyCycle(100)
                PWML.ChangeDutyCycle(100)
                time.sleep(1.75)
                PWMR.ChangeDutyCycle(0)
                PWML.ChangeDutyCycle(0)
            elif m == 1:
                m = 0

        if right == 1:
            right = 0
            PWMR.ChangeDutyCycle(100)
            PWML1.ChangeDutyCycle(100)
            time.sleep(.75)
            PWMR.ChangeDutyCycle(0)
            PWML1.ChangeDutyCycle(0)
            time.sleep(0.01)
            if m == 0:
                m = 1
                PWMR.ChangeDutyCycle(100)
                PWML.ChangeDutyCycle(100)
                time.sleep(1.75)
                PWMR.ChangeDutyCycle(0)
                PWML.ChangeDutyCycle(0)
            elif m == 1:
                m = 0
    return

mv_event = threading.Event()

communication = threading.Thread(name = 'comm', target = comm, args=(mv_event,))

tracker = threading.Thread(name = 'tracker', target = track, args=(mv_event,))

motor = threading.Thread(name = 'motor', target = mv_motor, args=(mv_event,))

communication.start()

time.sleep(1)

tracker.start()

motor.start()
