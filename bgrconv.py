#Author: 	Ross Barrett & Maheer Qahwash,
#Date: 		20/02/21
#Version:	1
#Description:	Converts BGR colour to HSV Colour with lower and upper bounds output to be used within the colourshow.py file


#Import system dependancies
import sys
import numpy as np
import cv2
 
#Take CLI Arguments and save them as vairables BGR vairables 
blue = sys.argv[1]
green = sys.argv[2]
red = sys.argv[3]  

#Convert to a unsigned numpy 8bit interger to HSV Colour using cvtcolour
rbgcolor = np.uint8([[[blue, green, red]]])
hsv_colour = cv2.cvtColor(rbgcolor, cv2.COLOR_BGR2HSV)
 
colourhue = hsv_colour[0][0][0]
 

#Generate an Print lower and upper bounds for range of colour detection
print("Lower bound is :"),
print("[" + str(colourhue-10) + ", 100, 100]\n")
 
print("Upper bound is :"),
print("[" + str(colourhue + 10) + ", 255, 255]")
