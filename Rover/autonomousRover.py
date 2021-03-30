# Pi Scouting Rover
# Autononous Rover
# VERSION 1.3
# Created by: Naa Kotey
# Date: 6/1/21
# UoG Advanced Computer Engineering 2020/21

import time
import RPi.GPIO as gpio
#import robohat
# Motors gpio pin assigmment
L1 = 36
L2 = 35
R1 = 33
R2 = 32

# servo gpio assignment
servo1 = 22
servo2 = 18

# ultrasonic gpio assignment
us = 38 #trigger and echo pins have the same output on the RoboHAT schematic

# speed of sound m/s
spos = int(343)

# gpio setup
# gpio.setmode(gpio.BCM) #broadcom alternative (may use for ultrasonic testing)
gpio.setmode(gpio.BOARD)
gpio.setup(L1, gpio.OUT)  # front left
gpio.setup(L2, gpio.OUT)  # back left wheel
gpio.setup(R1, gpio.OUT)  # Front right wheel
gpio.setup(R2, gpio.OUT)  # Back right Wheel
gpio.setup(servo1, gpio.OUT)  # Ultrasonic gimbal (bottom servo)
gpio.setup(servo2, gpio.OUT)  # Ultrasonic gimbal (top servo)

bottomPos = gpio.PWM(servo1, 200)
topPos = gpio.PWM(servo2, 200)

# Servo positions (based on testing with my set up; may change if screws
# are tightened)
left = 50 / 5
right = 250 / 5
centre = 150 / 5
up = 50 / 5
down = 150 / 5

# set default start position for the Ultrasonic - Centre facing
bottomPos.start(centre)
topPos.start(up)

# Servo Positioning Functions


def servoUpLeft():  # sets servo position upwards, pointing left
	print ("\nServo Position Left and Up")
	bottomPos.ChangeDutyCycle(left)
	topPos.ChangeDutyCycle(up)


def servoUpCentre():  # sets servo position upwards at the centre
	print ("\nServo Position Centre and Up")
	bottomPos.ChangeDutyCycle(centre)
	topPos.ChangeDutyCycle(up)


def servoUpRight():  # sets servo position upwards, pointing right
	print ("\nServo Position Right and Up")
	bottomPos.ChangeDutyCycle(right)
	topPos.ChangeDutyCycle(up)


def servoDownLeft():  # sets servo position downwards, pointing left
	print ("\nServo Position Left and Down")
	bottomPos.ChangeDutyCycle(left)
	topPos.ChangeDutyCycle(down)


def servoDownCentre():  # sets servo position downwards at the centre
	print ("\nServo Position Centre and Down")
	bottomPos.ChangeDutyCycle(centre)
	topPos.ChangeDutyCycle(down)


def servoDownRight():  # sets servo position downwards, pointing right
	print ("\nServo Position Right and Down")
	bottomPos.ChangeDutyCycle(right)
	topPos.ChangeDutyCycle(down)

# Motor Movement functions


def forward():  # causes Rover to indefinitely move forward unless another command is given
    gpio.output(L1, 1)
    gpio.output(L2, 0)
    gpio.output(R1, 1)
    gpio.output(R2, 0)


def reverse():  # causes Rover to indefinitely move backwards unless another command is given
    gpio.output(L1, 0)
    gpio.output(L2, 1)
    gpio.output(R1, 0)
    gpio.output(R2, 1)


def spinLeft():  # Sets the rover to spin anticlockwise
    gpio.output(L1, 0)
    gpio.output(L2, 1)
    gpio.output(R1, 1)
    gpio.output(R2, 0)


def spinRight():  # Sets the rover to spin clockwise
    gpio.output(L1, 1)
    gpio.output(L2, 0)
    gpio.output(R1, 0)
    gpio.output(R2, 1)


def stop():  # Disengages all wheels
    gpio.output(L1, 0)
    gpio.output(L2, 0)
    gpio.output(R1, 0)
    gpio.output(R2, 0)


def rigtManeuver():  # turns rover right to avoid a percieved obstacle
        stop()
        reverse()
        time.sleep(3)
        stop()
        spinRight()
        time.sleep(2)
        stop()
        '''forward()
        time.sleep(2)
        stop()'''
        return

def leftManeuver():  # turns rover left to avoid a percieved obstacle
        stop()
        reverse()
        time.sleep(3)
        stop()
        spinLeft()
        time.sleep(2)
        stop()
        '''forward()
        time.sleep(2)
        stop()'''
        return

# retreat - to be used if the rover hits a dead end where left, right and ahead is blocked
# reverses and attempts to go around perceived obstacle

def retreat():
        stop()
        reverse()
        time.sleep(3)
        stop()
        spinRight()
        time.sleep(2)
        forward()
        time.sleep(2)
        spinLeft()
        time.sleep(2)
        stop()
        forward()
        time.sleep(2)
        stop()
        return

# Ultrasonic functions


def ultrasonicDistance():  # calculates distance from objects ahead and determines if the way is clear
    sigLength =0
    while True:
        gpio.setup(us, gpio.OUT)  # Ultrasonic trigger
        gpio.output(us, True)
        time.sleep(0.00001)  # send pulse in 10 micro second blips
        gpio.output(us, False)
        sigStart = time.time()

        gpio.setup(us, gpio.IN)  # ultrasonic echo
        while gpio.input(us) == 0:  # count elapsed time between the sent and received signal
            sigStart = int(time.time())
        while gpio.input(us) == 1:
                sigEnd = int(time.time())
                sigLength = sigEnd - sigStart  # find total elapsed time
        # distance = speed of sound in air * time
        ultrasonicDist = int(spos * sigLength)
        
        if ultrasonicDist > 0.05: #m
            wayClear = True
        else:
            wayClear = False
    return wayClear
    
def wayClearLeft(): #Checks if left side is clear
    servoUpLeft()#set Ultrasonic Servo positon and take distance reading
    ultrasonicDistance()
    if wayClear == True:
            wayClearLeft = True
    else:
            wayClearLeft = False
    return wayClearLeft
            
    
def wayClearRight(): #Checks if right side is clear
    servoUpRight()#set Ultrasonic Servo positon and take distance reading
    ultrasonicDistance()
    if wayClear == True:
            wayClearRight = True
    else:
            wayClearRight = False
    return wayClearRight

# main
try:
        while True:
                ultrasonicDistance()
                if wayClear == True: #Check if the way is clear
                        forward()
                else:   #check if the left and right sides are clear
                        wayClearLeft()
                        wayClearRight()
                        if wayClearLeft == True and wayClearRight == False:
                                leftManeuver()
                        elif wayClearLeft == False and wayClearRight == True:
                                rightManeuver()
                        elif wayClearLeft == False and wayClearRight == False:
                                retreat()
                        else: #if all both left and right are clear, turn, with a preference to the right
                                rightManeuver()
except:
        gpio.cleanup()
