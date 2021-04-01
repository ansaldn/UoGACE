# moonBuggy

## Description
Scripts for various control functions of the cargo transportation Rover used on the Compound.

## Hardware Used
- Ultimate Initio Chassis kit for Raspberry Pi (https://shop.4tronix.co.uk/products/ultimate-initio-robot-kit-for-raspberry-pi?variant=36994821441)

- 4Tronix RoboHAT
- Raspberry Pi 3

![image](https://user-images.githubusercontent.com/73899520/112980812-42dc1f00-9152-11eb-9e4c-d2ed61aa816c.png)


## Installation
After assembly of the RoboHAT and chassis, open linux terminal and run the following commands to test sample code from the manufacturers of roboHAT. 

*Please note that these scripts aren't fully necessary to run the scripts in the rover folder, but are useful to test functionality of the Rover
```bash
if [ ! -d ~/robohat ]; then
  mkdir ~/robohat
fi
cd ~/robohat
wget -q http://4tronix.co.uk/robohat/servod.xxx -O servod
wget -q http://4tronix.co.uk/robohat/robohat.py -O robohat.py
wget -q http://4tronix.co.uk/robohat/motorTest.py -O motorTest.py
wget -q http://4tronix.co.uk/robohat/motorTest2.py -O motorTest2.py
wget -q http://4tronix.co.uk/robohat/motorTestRaw.py -O motorTestRaw.py
wget -q http://4tronix.co.uk/robohat/irTest.py -O irTest.py
wget -q http://4tronix.co.uk/robohat/servo.py -O servo.py
wget -q http://4tronix.co.uk/robohat/servoTest.py -O servoTest.py
wget -q http://4tronix.co.uk/robohat/sonarTest.py -O sonarTest.py
chmod +x servod
```
## Notable Scripts

### keyControlRover.py
- Remote Control feature
- Allows the Rover to be piloted via keystroke input.
- Allows manual setting of servo/ultrasonic position 

### autonomousRover.py
- Fully autonomous control and obstacle avoidance feature for the Rover
- Can be used for 'roaming'/exploration mode

Key functions include:

```python3
def ultrasonicDistance() 
```
This calculates the distance to the nearest obstacle based on calculations from the readings of the Ultrasonic Sensor

```python3
def wayClear() 
```
Based on the result of the previous function, this function determines whether the current path is clear and performs a sweep of the surroundings to seek an alternative route if it is obstructed.

### roverPark.py
- Parking sequence using Infrared sensors and line following to aim for precise positioning in the loading bay
- Includes use of pyserial to identify which base parking bay is being engaged

Key Functions Include:
```python3
def lineColour()
```
Determines whether or not the Rover has reached the parking bay, based on the expected IR reflectance value

### pathCorrection.py
- Corrects the path of the Rover if it's traversal starts becoming crooked
- Makes use of wheel sensor encoders
- Ideally for use right before parking

## Authors and Acknowledgement
Naa Kotey:
autonomousRover.py
roverPark.py
pathCorrection.py
lineFolTest.py

4Tronix:
robohat.sh

*Parts of the keyControlRover.py were inspired by the motor test script provided by 4Tronix
