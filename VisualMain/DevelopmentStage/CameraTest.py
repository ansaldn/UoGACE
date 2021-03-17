#Created By Ravi Kumar
#Date 26/02/2020
#Version:1
#Description: Camera and opencv testing and converting camera feed to grayscale and HSV
#import cv2 libraries
import cv2

#setting USb camera input 
cap = cv2.VideoCapture(0)
#frame width
cap.set(3, 640) 
#frame height
cap.set(4, 480)	
#frame brightness
cap.set(10,70) 

while(True):
	#Capturing image frame by frame
	ret, frame = cap.read()
	
	#frame operations 
	#coverting image captured in frame to grayscale and HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
	
	#Display all the resulting framse HSV, Greyscale and Color
	cv2.imshow('hsv', hsv)
	cv2.imshow('gray' ,gray)
	cv2.imshow('color', frame)
	
	#Stop the program and close the resulting frame with key press 'Q'
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

#release the capture and close all windows 
cap.release()
cv2.destroyAllWindows()
