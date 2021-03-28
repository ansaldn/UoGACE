#Author: 	Ross Barrett & Maheer Qahwash,
#Date: 		20/02/21
#Version:	1
#Description:	Displays the colour converted image of a specified colour defined by the HSV output from bgrconv.py

#import system dependancies
import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while(1):

    # Read in every frame in camera
    _, frame = capture.read()

    # Convert BGR to HSV
    colour = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of color in HSV (output from bgrconv.py)
    lower_colourrange = np.array([161,100,100])
    upper_colourrange = np.array([181,255,255])

    # Set the threshold of the video to output specified colour range
    mask = cv2.inRange(colour, lower_colourrange, upper_colourrange)

    # Use Bitwise-AND command to set mask and the original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    #display the 3 windows (frame, mask, res) and wait for esc key or ctrl+c to end program
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    key = cv2.waitKey(1) & 0xFF
 
    # upon x key being pressed, stop the script
    if key == ord("x"):
        break


#close all windows opened by program
cv2.destroyAllWindows()
