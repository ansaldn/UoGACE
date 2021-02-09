#Created by Maher
#Date: 04/02/2021
#Description: Alternative way for openCV video input

#input depandencies

import cv2
#Configure Camera Reesolution
frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture("Desktop/Maher_test_ videov1.mp4")
#Statement to Play video break on q press
while True:
    success, img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
         break
