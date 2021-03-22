# moonBuggy

## Description
Scripts for various control functions of the cargo transportation Rover used on the Compound.

## Hardware 
- Ultimate Initio Chassis kit for Raspberry Pi (https://shop.4tronix.co.uk/products/ultimate-initio-robot-kit-for-raspberry-pi?variant=36994821441)

- 4Tronix RoboHAT
- Raspberry Pi 3

## Installation
After assembly of the RoboHAT and chassis, open linux terminal and run the following commands to test sample code from the manufacturers of roboHAT. 

*Please note that these scripts aren't fully necessary to run the scripts in the rover folder, but are useful to test functionality of the Rover

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
Determines the colour of the parking bay based on the expected IR reflectance value

### pathCorrection.py
- Corrects the path of the Rover if it's traversal starts becoming crooked
- Makes use of wheel sensor encoders
- Ideally for use right before parking


## Contributing

## Authors and Acknowledgement

## License
