# Pi Scouting Rover
# Keyboard input
# VERSION 1.0
# Created by: Naa Kotey
# Date: 12/12/20

import time
import RPi.GPIO as gpio
import curses as key

# keystroke input

screen = key.initscr()
key.noecho()
key.cbreak()
screen.keypad(True)

#Motors gpio pin assigmment
L1 = 36
L2 = 35
R1 = 33
R2 = 32

# servo gpio assignment
servo1 = 22
servo2 = 18

#gpio setup
gpio.setmode(gpio.BOARD)
gpio.setup(L1, gpio.OUT) # front left
gpio.setup(L2, gpio.OUT) # back left wheel
gpio.setup(R1, gpio.OUT) # Front right wheel
gpio.setup(R2, gpio.OUT) #Back right Wheel
gpio.setup(servo1, gpio.OUT) # servo1
gpio.setup(servo2, gpio.OUT) #servo2
#Servo control
bottomPos = gpio.PWM(servo1, 200)
topPos = gpio.PWM(servo2, 200)

#positions
left = 25/5
right = 150/5
centre = 50/5
up = 50/5
down = 150/5

bottomPos.start(centre)
topPos.start(up)

def servoUpLeft():
	print ("\nServo Position Left and Up")
	bottomPos.ChangeDutyCycle(left)
	topPos.ChangeDutyCycle(up)

def servoUpCentre():
	print ("\nServo Position Centre and Up")
	bottomPos.ChangeDutyCycle(centre)
	topPos.ChangeDutyCycle(up)

def servoUpRight():
	print ("\nServo Position Right and Up")
	bottomPos.ChangeDutyCycle(right)
	topPos.ChangeDutyCycle(up)

def servoDownLeft():
	print ("\nServo Position Left and Down")
	bottomPos.ChangeDutyCycle(left)
	topPos.ChangeDutyCycle(down)

def servoDownCentre():
	print ("\nServo Position Centre and Down")
	bottomPos.ChangeDutyCycle(centre)
	topPos.ChangeDutyCycle(down)

def servoDownRight():
	print ("\nServo Position Right and Down")
	bottomPos.ChangeDutyCycle(right)
	topPos.ChangeDutyCycle(down)

#Motor Movement functions
def forward():
    gpio.output(L1, 1)
    gpio.output(L2, 0)
    gpio.output(R1, 1)
    gpio.output(R2, 0)

def reverse():
    gpio.output(L1, 0)
    gpio.output(L2, 1)
    gpio.output(R1, 0)
    gpio.output(R2, 1)

def spinLeft():
    gpio.output(L1, 0)
    gpio.output(L2, 1)
    gpio.output(R1, 1)
    gpio.output(R2, 0)

def spinRight():
    gpio.output(L1, 1)
    gpio.output(L2, 0)
    gpio.output(R1, 0)
    gpio.output(R2, 1)

def stop():
    gpio.output(L1, 0)
    gpio.output(L2, 0)
    gpio.output(R1, 0)
    gpio.output(R2, 0)


#main
try:
	while True:
		char = screen.getch()
		if char == 120: #x
			break
		elif char == key.KEY_UP:
	    		print ("Forward")
			forward()
		elif char == key.KEY_DOWN:
	    		print ("Reverse")
			reverse()
		elif char == key.KEY_RIGHT:
	    		print ("Right")
			spinRight()
		elif char == key.KEY_LEFT:
	    		print ("Left")
			spinLeft()
		elif char == 32: #spacebar
	    		print ("Stop")
			stop()
		elif char == 119: #w (servo up centre):
			servoUpCentre()
		elif char == 113: #q
			servoUpLeft()
		elif char == 101: #e
			servoUpRight()
		elif char == 97: #a
			servoDownLeft()
		elif char == 115: #s
			servoDownCentre()
		elif char == 100: #d
			servoDownRight()
finally:
    key.nocbreak(); screen.keypad(0); key.echo()
    key.endwin()
    gpio.cleanup()

