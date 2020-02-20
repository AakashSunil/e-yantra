import numpy as np
import cv2

def findCheckPointColour(img):             ## You can pass your own arguments in this space.
    dim = img.shape
    # red marker         
    red_low_bound0 = np.array([175, 100, 100])
    red_up_bound0 = np.array([180, 255, 255])
    red_low_bound1 = np.array([0, 100, 100])
    red_up_bound1 = np.array([10, 255, 255])

    red_mask1 = cv2.inRange(img, red_low_bound0, red_up_bound0)
    red_mask2 = cv2.inRange(img, red_low_bound1, red_up_bound1)
    red_mask = red_mask1 | red_mask2

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if red_mask[i,j]>127:
                return "Red" #1
    
    
    # blue marker
    blue_low_bound = np.array([130, 100, 100])
    blue_up_bound = np.array([150, 255, 255])

    blue_mask = cv2.inRange(img, blue_low_bound, blue_up_bound)

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if blue_mask[i,j]>127:
                return "Blue" #2
            
    # sky blue marker
    sblue_low_bound = np.array([90, 100, 100])
    sblue_up_bound = np.array([120, 255, 255])

    sblue_mask = cv2.inRange(img, sblue_low_bound, sblue_up_bound)

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if sblue_mask[i,j]>127:
                return "Cyan"

    # pink marker
    pink_low_bound = np.array([145, 100, 100])
    pink_up_bound = np.array([170, 255, 255])
    
    pink_mask = cv2.inRange(img, pink_low_bound, pink_up_bound)

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if pink_mask[i,j]>127:
                return "Pink"
            
    # green marker
    green_low_bound = np.array([50, 100, 100])
    green_up_bound = np.array([70, 255, 255])
    
    green_mask = cv2.inRange(img, green_low_bound, green_up_bound)

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if green_mask[i,j]>127:
                return "Green"
            
    # yellow marker
    yellow_low_bound = np.array([25, 100, 100])
    yellow_up_bound = np.array([35, 255, 255])
    
    yellow_mask = cv2.inRange(img, yellow_low_bound, yellow_up_bound)

    for i in range(0,dim[0],5):
        for j in range(0,dim[1],5):
            if yellow_mask[i,j]>127:
                return "Yellow"
            
    # white marker
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret,white_mask = cv2.threshold(grayImg,50,255,cv2.THRESH_BINARY_INV)

    for i in range(5,dim[0]-5,5):
        for j in range(5,dim[1]-5,5):
            if red_mask[i,j]<127:
                return "White"
                
cap = cv2.VideoCapture(0)

def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = cap.read()
 return im

while True:
# Capture frame-by-frame
    ret, frame = cap.read()
    for i in xrange(30):
        temp = get_image()
# Our operations on the frame come here

    frame = get_image()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    colour = findCheckPointColour(hsv)
    print colour
# Display the resulting frame
    cv2.imshow('frame',hsv)
    
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
