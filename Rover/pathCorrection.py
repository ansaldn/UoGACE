#pathCorrection
#Author: Naa Kotey
#Date: 18/03/21
#Version: 1.0

'''
- Script to correct path of the Rover if it veers off course
- Measure wheel diameter;calculate wheel circunmference
- One revolution will equal x m travelled
- Bases are a fixed distance apart; approximate how many rotations to cover the distance between bases
- Balance  wheel count on each side if there's a difference of more than 3 clicks
'''
import time
import keyControlRover.py #import previous script
import RPi.GPIO as gpio
import math

#pin assignment
encL = 15 #Left wheel Encoder
encR =  16 #Right wheel Encoder

gpio.setmode(gpio.BOARD)
gpio.setup(encL, gpio.IN)#set as inputs
gpio.setup(encR, gpio.IN)

#quantities for distance calculation
spokes = int (18) #number of spokes on each wheel encoder
diameter = float(0.053) #wheel diameter - meters
crcmf = float(diameter)*math.pi #wheel circumference = pi*diameter
clicksL = 0 #number of spokes recorded on left wheel
clicksR = 0 #number of spokes recorded on right wheel
clicksDiff = int(clicksL)-int(clicksR)
rotations =  int(int(clicksL)/spokes) #number of complete rotations
disTravelled = round((rotations*crcmf),2) #meters
prevLState = gpio.input(encL) #previous state of encoder (high or low)
prevRState = gpio.input(encR)

def leftBiasCorrect():#straightens if rover is tilting left
    while clicksDiff != 0:
        stop()
        spinRight()
        time.sleep(0.01)
        stop()

def rightBiasCorrect():#straightens if rover is tilting right
    while clicksDiff != 0:
        stop()
        spinLeft()
        time.sleep(0.01)
        stop()

def straight():
    #wheelCount()
    if clicksDiff >= 3:
        isStraight = False
        print ("Rover straying Left; correcting")
        #print("stop left side/ turn right a bit until clicksDiff = 0")
        leftBiasCorrect()
    elif clicksDiff <= -3:
        isStraight = False
        print ("Rover straying Right; correcting")
        #print("stop right side/ turn left a bit until clicksDiff = 0")
        rightBiasCorrect()       
    else:
        isStraight = True
    print('Rover Straight? ', isStraight)

'''def setCourse():
    if location = 'Base1':
        destination = 'Base2'
        print ('Heading to ', destination) #change this to echo in bash
    elif location = 'Base2':
        destination = 'Base1'
        print ('Heading to ', destination) #change this to echo in bash
    else:
        break
'''        
        
def wheelCount():
    #count rotations
    while True:
        LState = gpio.input(encL) #current state; Left sensor
        RState = gpio.input(encR) #current state; Right Sensor
        if LState != prevLState:
            clicksL += 1
        elif RState != prevRState:
            clicksR += 1
        else:
            clicksR = clicksR
            clicksL = clicksL
        print (rotations, disTravelled)
        sleep(0.01)
    
def main():
    while True:
        #setCourse()
        wheelCount()
        forward()
        time.sleep(2)
        straight()
        time.sleep(1)
             
try:
    main()

except:
    gpio.cleanup()
