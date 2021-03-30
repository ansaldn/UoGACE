#roverPark
#Author: Naa Kotey
#Date: 17/03/21
#Version 1.1

#line following/detecting script to initiate parking sequence

import time
import keyControlRover
import pathCorrection
import RPi.GPIO as gpio
import math

#gpio setup for line following sensors
lineFolL =29
lineFolR =13

gpio.setmode(GPIO.BOARD)
gpio.setup(lineFolL, gpio.IN)
gpio.setup(lineFolR, gpio.IN)

location = 'Transit' # transit, base1, base2 or home
parked = False #parked state
bay = False #reached parking bay?

def base1Park(): #Maneuver to position the rover for unloading
    stop()
    straight()#align to straighten park
    reverse()
    time.delay(0.3)
    stop()
    clicksL = 0 #reset click count
    clicksR = 0
    
    while clicksL <= 9: #half one full rotation
        spinLeft()
        
    stop()    
    reverse()
    time.delay(0.1)
    stop()
    parked = True

def base2Park(): #Maneuver to position the rover for loading/unloading
    stop()
    straight()#align to straighten park
    reverse()
    time.delay(0.3)
    stop()
    clicksL = 0 #reset click count
    clicksR = 0
    
    while clicksR <= 9: #half one full rotation
        spinRight() #spin 180degrees
        
    stop()
    reverse()
    time.delay(0.1)
    stop()
    parked = True

def lineColour(): #detect line colour (senses reflectivity)
    '''maxRflc = peak reflectance value 
    minRflc = #min reflectance value 
    avgrflc = int(maxRflc) - int(minRflc)
    if avgrflc >= (num) and avgrflc >= (num) #IR reflectivity is in a certain range:'''
    
    if gpio.input(lineFolL) == False and gpio.input(lineFolR) == False:
        bay = True
        colour = 'black'
    elif gpio.input(lineFolL) == True and gpio.input(lineFolR) == True:
        bay = True
        colour = 'white'
    else:
        bay = False
        colour = 'N/A'
    return bay
    return colour

def main():
    while True:

        lineColour()
        if bay == True and colour == 'black':
            location = 'Base1'
            base1Park()
            print("Parked at Base1")#replace with echo bash script
               
        elif bay == True and colour == 'white':
            location = 'Base2'
            base2Park()
            print("Parked at Base2")#replace with echo bash script
        else:
            bay == False
            location = 'Transit'
            #continue travel
        time.sleep(0.01)

try:
    main()
    
except:
    gpio.cleanup()
