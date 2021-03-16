#Author:Ross Barrett
#Date: 15/01/2021
#Description: Basic Script to test Camera input & CV2 installation 


#Import CV2 Libary.
import cv2

#Webcam resolution settings.
frameWidth = 640
frameHeight = 480

#Set Cap to USB video camera input 0=Webcam 1, 1=Webcam 2. 
cap = cv2.VideoCapture(1)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)
#Allways show video and allow for program break with key Press Q
while True:
    success, img = cap.read()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break
