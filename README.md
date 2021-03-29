# Advanced Computer Engineering Project

## Software and Hardware used
Hardware used for this project: 
 - [x] Single Board Computers : Raspberry Pi, Jetson Nanos, Odriod
 - [x] Two Robotic Arms
 - [x] Range of sensors and actuator
                                
Software used for this project: Python

## Quick Install
To get started, you will need to download this repository to do so, download GitHub onto your raspberry pi using the following command:

```bash
sudo get install git -y
```
When this is complete, clone the relevant branches to the relevant Pis. Use this command to do so:
```bash
git clone github.com/da5905p/UoGACE/--BRANCH NAME--
```
*Where you change --BRANCH NAME-- for the relevenat branch i.e. Network, GUI.*

Note: Not all Pis need all branches to function. The list of which pis are required for which systems are below.

TouchScreen Pi = GUI, Network  
moonBuggy Pi = moonBuggy, Visual, Network  
Bases = Arm, Visual, Network  

## Description
The project was sectioned in multiple branches and multiple teams which received a small task to reach the final result. There are 8 branches: moonBuggy, Arm, Network, Visual, GUI, baseNavigation, testBranch and Environment-&-Dependancies branch. The main goal of this project was to use the available hardware to design and program a functionable robot which, as a short brief, will be able to use movement functions for the base and it will move around collecting what it detects from the storage; after finding the object using image detection, it will be able to grab that object and deposit it onto the car and also from the car to the storage. 

An image of the robot after it was put together will be attached:

![image](https://user-images.githubusercontent.com/75362937/112773379-c94b1080-902d-11eb-881e-bcc51d90ea0e.png)

### Arm Control
The main purpose of the Arm branch was to develop a code which will give the user the possiblity to control the arm remotely. The arm is able to rotate in any direction, rise up and down and different other functions. At the end of the physical arm, a claw is present which will be used to grab and also drop things from a certain location to another location, which is the storage, and vice versa.

There are different movements possible: GripsOpen, GripsClose, WristUp, WristDown, ElbowUp, ElbowDown, ShoulderUp, ShoulderDown, Stop etc. 

As an example: 

```bash
>>> arm.move(usb_arm.GripsOpen)
```
The grips will open.

Programmed sequence of actions can be created for this, these sequences being multiple arrays of commands as seen in the following example:

```bash
rotate = [[usb_arm.BaseCtrClockWise,7],[usb_arm.GripsOpen],[usb_arm.BaseClockWise,6.8]]
```

And to run the action: 

```bash
arm.doActions(rotate)
```

### Image Detection

### Network 
This branch will allow the different devices to connect with each other and at the same time, whenever a device is sending information it will encrypt it and when it receives it, it will decrypt it. The Network is one of the most important one since it makes the whole system working together possible. 

To assure the security of the network, the use of crypthographic keys was necessary. For this project, Fernet was used to provide the keys, this being an implementation of symmetric authenticated cryptography:

```bash
from cryptography.fernet import Fernet
key = Fernet.generate_key()
```

The command will provide a URL-safe base64-encoded 32-byte key.

## Authors and aknowledgements

## License
