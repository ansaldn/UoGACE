#Author: 	Ross Barrett & Maheer Qahwash,
#Date: 		20/02/21
#Version:	1
#Description:	Converts RGB colour to HSV Colour with lower and upper bounds output to be used within the colourshow.py file


#Import system dependancies
import sys
import numpy as np
import cv2

#If statement to look for if an argument has been passed to the file
if not len(sys.argv) > 1:
    print("Please enter RGB value into command line as arguments, Use following format:Python3 RGBConvert.py Redvalue GreenValue BlueValue")
else:
    #Take Command Line Arguments and save them as RGB vairables 
    red = sys.argv[1]
    green = sys.argv[2]
    blue = sys.argv[3]
 

    #Convert to a unsigned numpy 8bit interger to HSV Colour using cvtcolour
    #convert RGB to BGR for use with BGR 2 HSV OpenCV command
    rbgcolour = np.uint8([[[blue, green, red]]])
    hsv_colour = cv2.cvtColor(rbgcolour, cv2.COLOR_BGR2HSV)
 
    colourhue = hsv_colour[0][0][0]

    #Generate an Print lower and upper bounds for range of colour detection
    print("Lower bound for tracking is :"),
    print("[" + str(colourhue-10) + ", 100, 100]\n")
 
    print("Upper bound for tracking is :"),
    print("[" + str(colourhue + 10) + ", 255, 255]")
