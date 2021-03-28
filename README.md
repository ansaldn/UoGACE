# Advanced Computer Engineering Project

## Software and Hardware used
Hardware used for this project: 
 - [x] Single Board Computers : Raspberry Pie, Jetson Nanos, Odriod
 - [x] Two Robotic Arms
 - [x] Range of sensors and actuator
                                
Software used for this project: Python
## Getting Started

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

## Usage

## Arm Control
The main purpose of the Arm branch was to develop a code which will give the user the possiblity to control the arm remotely. The arm is able to rotate in any direction, rise up and down and different other functions. At the end of the physical arm, a claw is present which will be used to grab and also drop things from a certain location to another location, which is the storage, and vice versa.

There are different movements possible: GripsOpen, GripsClose, WristUp, WristDown, ElbowUp, ElbowDown, ShoulderUp, ShoulderDown, Stop etc. 

As an example: 

```bash
>>> arm.move(usb_arm.GripsOpen)
```
The grips will open.

## Image Detection

## Running the program

## Authors and aknowledgements

## License
