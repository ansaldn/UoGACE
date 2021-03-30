# Pi Scouting Rover
# Keyboard input
# VERSION 1.2
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

# Motors gpio pin assigmment
L1 = 36
L2 = 35
R1 = 33
R2 = 32

# servo gpio assignment
servo1 = 22
servo2 = 18

# gpio setup
gpio.setmode(gpio.BOARD)
gpio.setup(L1, gpio.OUT)  # front left
gpio.setup(L2, gpio.OUT)  # back left wheel
gpio.setup(R1, gpio.OUT)  # Front right wheel
gpio.setup(R2, gpio.OUT)  # Back right Wheel
gpio.setup(servo1, gpio.OUT)  # servo1
gpio.setup(servo2, gpio.OUT)  # servo2
# Servo control
bottomPos = gpio.PWM(servo1, 200)
topPos = gpio.PWM(servo2, 200)

# servo positions
left = 250/ 5
right = 50 / 5
centre = 150 / 5
up = 50 / 5
down = 150 / 5

#start in central posotion
bottomPos.start(centre)
topPos.start(up)


def servoUpLeft(): #sets servo upwards and to the left
    print ("\nServo Position Left and Up")
    bottomPos.ChangeDutyCycle(left)
    topPos.ChangeDutyCycle(up)


def servoUpCentre(): #sets servo upwards and central
    print ("\nServo Position Centre and Up")
    bottomPos.ChangeDutyCycle(centre)
    topPos.ChangeDutyCycle(up)


def servoUpRight(): #sets servo upwards and to the right
    print ("\nServo Position Right and Up")
    bottomPos.ChangeDutyCycle(right)
    topPos.ChangeDutyCycle(up)


def servoDownLeft(): #sets servo downwards and to the left
    print ("\nServo Position Left and Down")
    bottomPos.ChangeDutyCycle(left)
    topPos.ChangeDutyCycle(down)


def servoDownCentre(): #sets servo downwards central
    print ("\nServo Position Centre and Down")
    bottomPos.ChangeDutyCycle(centre)
    topPos.ChangeDutyCycle(down)


def servoDownRight(): #sets servo downwards and to the right
    print ("\nServo Position Right and Down")
    bottomPos.ChangeDutyCycle(right)
    topPos.ChangeDutyCycle(down)

# Motor Movement functions

def forward(): #sends rover forwards
    gpio.output(L1, 1)
    gpio.output(L2, 0)
    gpio.output(R1, 1)
    gpio.output(R2, 0)


def reverse(): #sends rover backwards
    gpio.output(L1, 0)
    gpio.output(L2, 1)
    gpio.output(R1, 0)
    gpio.output(R2, 1)


def spinLeft(): #turns rover left on the spot
    gpio.output(L1, 0)
    gpio.output(L2, 1)
    gpio.output(R1, 1)
    gpio.output(R2, 0)


def spinRight(): #turns rover right on the spot
    gpio.output(L1, 1)
    gpio.output(L2, 0)
    gpio.output(R1, 0)
    gpio.output(R2, 1)


def stop(): #disengages wheels
    gpio.output(L1, 0)
    gpio.output(L2, 0)
    gpio.output(R1, 0)
    gpio.output(R2, 0)


# main
try:
    while True:
        char = screen.getch()
        if char == 120:  # key x
            break

        elif char == key.KEY_UP: #up key
            print ("Forward")
            forward()

        elif char == key.KEY_DOWN: #down key
            print ("Reverse")
            reverse()

        elif char == key.KEY_RIGHT: #right key
            print ("Right")
            spinRight()

        elif char == key.KEY_LEFT: #left key
            print ("Left")
            spinLeft()

        elif char == 32:  # spacebar
            print ("Stop")
            stop()

        elif char == 119:  # key w
            servoUpCentre()

        elif char == 113:  # key q
            servoUpLeft()

        elif char == 101:  # key e
            servoUpRight()

        elif char == 97:  # key a
            servoDownLeft()

        elif char == 115:  # key s
            servoDownCentre()

        elif char == 100:  # key d
            servoDownRight()

finally:
    key.nocbreak()
    screen.keypad(0)
    key.echo()
    key.endwin()
    gpio.cleanup()
