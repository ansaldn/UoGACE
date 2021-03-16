#Created By Maher and Ross
#Date: 26/02/2021
#Description: Object colour detection and tracking using colour bounds with OpenCV & Python3
#Version:1.0 (Release)

# import required packages
from collections import deque
import numpy as np
import imutils
import cv2

#Construct the map position objety with type value x & y
def createobjectxandy (x, y):
    print ("Object Coordinates at X = {0} and Y =  {1}".format(x, y))

# Set upper and lower limits of the object to be tracked bounds 
# To be generated from Output from BGRconvert.py see Github
colourLower = (53, 100, 100)
colourUpper = (73, 255, 255)

 
# Get the Video camera feed of webcam 1
webcam = cv2.VideoCapture(0)

# keep looping
while True:
    # capture the current video frame
    (grabbed, vid) = webcam.read()
 
    #convert the frame from BGR to HSV
    hsvcolour = cv2.cvtColor(vid, cv2.COLOR_BGR2HSV)
 
    # convert the mask for the colour specified by the colour bounds 
    # remove the outliers in the mask using erode and dilate
    convertedmask = cv2.inRange(hsvcolour, colourLower, colourUpper)
    convertedmask = cv2.erode(convertedmask, None, iterations=2)
    convertedmask = cv2.dilate(convertedmask, None, iterations=2)
    
    # use cv2.findContours to locate contours
    contours = cv2.findContours(convertedmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    # initialize the center of tracked colour/object
    contourcenter = None
 
    # if statement looking for one contour is found in contour que
    if len(contours) > 0:
        # Take the last contour from the contour que,
        # compute the size of the circle to be drawn
        c = max(contours, key=cv2.contourArea)
        ((x, y), rad) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        contourcenter = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
        # continue if the radius meets a minimum size
        if rad > 10:
            # place circle around the contour point,
            # update the x and y of the the center point
            cv2.circle(vid, (int(x), int(y)), int(rad),
                (255, 255, 255), 3)
            cv2.circle(vid, contourcenter, 4, (10, 255, 255), -1)

	    # print center of circle coordinates
            createobjectxandy(int(x), int(y))
 
    # update queue of x and y co-ordinates using deque command
    deque([]).appendleft(contourcenter)
 
    # show the video stream
    cv2.imshow("ADV Comp ENG 1 Oject Colour Tracking", vid)
    key = cv2.waitKey(1) & 0xFF
 
    # upon x key being pressed, stop the script
    if key == ord("x"):
        break

#End of file
