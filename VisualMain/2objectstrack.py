#Created By Maher, Ross and Ravi 
#Date: 26/02/2021
#Description: Tracking of 1 object and 1 Vehicle based on 2 different colours
#Version:1.1 (Release as of 17/03/21)
#Update 1.1:Fixed Co-ordinates not being printed when only 1 object is in frame & Updated comments

# import required packages
from collections import deque
import numpy as np
import imutils
import cv2

#Construct the definition to print object position value x & y
def createobjectxandy (x, y):
    print ("Object at X = {0} and Y =  {1}".format(x, y))

#Construct the definition to print car position value x & y
def carcreateobjectxandy (x, y):
    print ("Car at X = {0} and Y =  {1}".format(carx, cary))


# Set upper and lower limits of the object to be tracked bounds 
# To be generated from Output from BGRconvert.py see Github
object1Lower = (8, 100, 100)
object1Upper = (28, 255, 255)
carlower = (160, 100, 100)
carupper = (180, 255, 255)
 
# Get the Video camera feed of webcam 1
webcam = cv2.VideoCapture(0)

# keep looping
while True:

    # capture the current video frame
    (grabbed, vid) = webcam.read()
 
    #convert the frame from BGR to HSV for object 1 
    obj1hsvcolour = cv2.cvtColor(vid, cv2.COLOR_BGR2HSV)
    
    #convert the frame from BGR to HSV for car object 
    carhsvcolour = cv2.cvtColor(vid, cv2.COLOR_BGR2HSV)

    # convert the mask for the colour specified by the colour bounds 
    # remove the outliers in the mask using erode and dilate
    convertedmask = cv2.inRange(obj1hsvcolour, object1Lower, object1Upper)
    convertedmask = cv2.erode(convertedmask, None, iterations=2)
    convertedmask = cv2.dilate(convertedmask, None, iterations=2)
    carconvertedmask = cv2.inRange(carhsvcolour, carlower, carupper)
    carconvertedmask = cv2.erode(carconvertedmask, None, iterations=2)
    carconvertedmask = cv2.dilate(carconvertedmask, None, iterations=2)

    # use cv2.findContours to locate contours of object1contours
    obj1contours = cv2.findContours(convertedmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    # CAR use cv2.findContours to locate contours of carcontours
    carcontours = cv2.findContours(carconvertedmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    
    # initialize the center of tracked colours/objects
    obj1contourcenter = None
    carcontourcenter = None

    # if statement looking for one contour is found in contour que
    if len(obj1contours) > 0 and len(carcontours) <= 0:

        # Take the last contour from the contour que,
        # compute the size of the circle to be drawn
        c = max(obj1contours, key=cv2.contourArea)
        ((x, y), rad) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        obj1contourcenter = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

	#If the largest circle's radius in mask is greater than 10px (Object1)  
        if rad > 10:

            # place circle around the contour point,
            # update the x and y of the the center point
            cv2.circle(vid, (int(x), int(y)), int(rad),
                (255, 255, 255), 3)
            cv2.circle(vid, obj1contourcenter, 4, (10, 255, 255), -1)

	# print object coordinates
        createobjectxandy(int(x), int(y))
        
	#ElseIf looking for array legnth of objects 
    elif len(obj1contours) <= 0 and len(carcontours) > 0:

        # Take the last contour from the contour que,
        # compute the size of the circle to be drawn
        car = max(carcontours, key=cv2.contourArea)
        ((carx, cary), carrad) = cv2.minEnclosingCircle(car)
        Mcar = cv2.moments(car)
        carcontourcenter = (int(Mcar["m10"] / Mcar["m00"]), int(Mcar["m01"] / Mcar["m00"]))  

	#If the largest circle's radius in mask is greater than 10px (CAR)  
        if  carrad > 10:

            # place circle around the contour point,
            # update the x and y of the the center point
            cv2.circle(vid, (int(carx), int(cary)), int(carrad),
                (255, 255, 255), 3)
            cv2.circle(vid, carcontourcenter, 4, (10, 255, 255), -1)

	# print car coordinates
        carcreateobjectxandy(int(carx), int(cary))

	#ElseIf looking if array legnth of Both objects is > 0
    elif  len(carcontours) > 0 and len(obj1contours) > 0:

        # Take the last contour from the contour que,
        # compute the size of the circle to be drawn
        car = max(carcontours, key=cv2.contourArea)
        ((carx, cary), carrad) = cv2.minEnclosingCircle(car)
        Mcar = cv2.moments(car)
        carcontourcenter = (int(Mcar["m10"] / Mcar["m00"]), int(Mcar["m01"] / Mcar["m00"]))
        c = max(obj1contours, key=cv2.contourArea)
        ((x, y), rad) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        obj1contourcenter = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))


	#If the largest circle's radius in mask is greater than 10px (Both Objects)  
        if rad > 10 and carrad > 10:

	    # place circle around the contour point,
            # update the x and y of the the center point
            cv2.circle(vid, (int(carx), int(cary)), int(carrad),
                (255, 255, 255), 3)
            cv2.circle(vid, carcontourcenter, 4, (10, 255, 255), -1)
            cv2.circle(vid, (int(x), int(y)), int(rad),
                (255, 255, 255), 3)
            cv2.circle(vid, obj1contourcenter, 4, (10, 255, 255), -1)

	# print object1 and car coordinates
        carcreateobjectxandy(int(carx), int(cary))
        createobjectxandy(int(x), int(y))

    # update queue of x and y co-ordinates and remove 1 entry using deque command
    deque([]).appendleft(obj1contourcenter)
    deque([]).appendleft(carcontourcenter)


    # show the video stream
    cv2.imshow("ADV Comp ENG 1 Oject Colour Tracking", vid)
    key = cv2.waitKey(1) & 0xFF
 
    # upon x key being pressed, stop the script
    if key == ord("x"):
        break

#End of file
