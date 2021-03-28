#Created By :Ravi Kumar
#Date Created : 06/02/2021
#Version 1.0
#Description : Detects any foreign object that is introduced in the frame
#imporing the rquired libraries
import cv2
import imutils

#setting USB camera port
cap = cv2.VideoCapture(0)
#declaring variables
average = None
imgname = 0
movementCounter = 0
minCounter = 10

#naming the output window and making it resizeable
cv2.namedWindow('Object_Detection', cv2.WINDOW_NORMAL)

#creating a while loop where the base frame is set
while True:
	#configuring the frame to capture frame by frame
	ret, frame = cap.read()
	#initial frame set up 
	frame = cv2.resize(frame, (1080,720), interpolation = cv2.INTER_LINEAR)
	#converting to grayscale
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#Gausian filter is used to clear the image
	gray = cv2.GaussianBlur(gray, (19, 19), cv2.BORDER_DEFAULT)
	
	if average is None:
		print("[DATA] starting background model...")
		average = gray.copy().astype("float")
		continue	

	#backgroud is updated after the accumulation of average weight 
	cv2.accumulateWeighted(gray, average, 0.7)
	#delta frame is set to calulate the pixel difference between each image
   	# object is detected when the new frame is subtracted from the initial frame and the difference in the pixels is the new object detected
	frameDelta =cv2.absdiff(gray, cv2.convertScaleAbs(average))
	
	#delta image is assigned a threshhold 
	thresh = cv2.threshold(frameDelta , 5 , 255 , cv2.THRESH_BINARY)[1]
	#image is dilated
	thresh = cv2.dilate(thresh, None, iterations=2)
	#finding contours on the threshold images
	cntrs = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	cntrs = imutils.grab_contours(cntrs)

	#creating a loop for contours
	for c in cntrs:

		#contours of small sizes are to be neglected and program should progress forward
		if cv2.contourArea(c) < 10000:
			continue
	
		#computing and drawing rectangular box for contour 
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x,y), (x + w, y + h), (255 ,0 , 0) , 3)
		#updating the info
		text = "OBJECT DETECTED"

		#adding text to the frame
		cv2.putText(frame , text, (20,30),
		cv2.FONT_HERSHEY_PLAIN, 2 ,(0, 0, 255) ,4)
		
		#when movement is detected a snap of the frame is saved and the movement counter resets to detect new changes
		movementCounter = movementCounter+1
		if(movementCounter>=minCounter):
			imgname=imgname+1
			#Setting the directory for saving data
			cv2.imwrite('./collection/{}.jpg'.format(imgname),frame)
			movementCounter=0

	#display the camera feed 
	cv2.imshow("Object_Detection", frame)
	key =cv2.waitKey(1) & 0xFF

	#Stop the feed and break the loop with key press 'Q'
	if key == ord("q"):
		break

#releae all capture and kill current windows in prep for next frame
cap.release()
cv2.destroyALLWindows()
