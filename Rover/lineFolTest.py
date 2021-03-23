#Line Follow Functionality test
#Author: Naa Kotey
#Date: 22/03/21
#Version 1.0


import time
import RPi.GPIO as gpio

#gpio set up
lineFolL =29
lineFolR =13

gpio.setmode(GPIO.BOARD)
gpio.setup(lineFolL, gpio.IN)
gpio.setup(lineFolR, gpio.IN)

try:
	while True: #prints state of line following sensors
            print ("Left", gpio.input(lineFolL))
            time.sleep(0.01)
            print ("Right ", gpio.input(lineFolR))
            time.sleep(0.0.1)
            
		'''if not gpio.input(lineFolR):
			print("Straying Left")
			
		elif not gpio.input(lineFolL):
			print("Straying Right")
		else:
			print("Following line")
		sleep(0.1)'''
except:
	GPIO.cleanup()
