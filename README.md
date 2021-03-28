# Advanced Computer Engineering Project
Documentation of the python code used in the Arm Branch of the ACE project.

## Software and Hardware used
Hardware used for this project: 
 - [x] Single Board Computers : Raspberry Pie, Jetson Nanos.
 - [x] Two Robotic Arms


 Language used for this project: Python and C++.  
 Software used: Notepad, Nano and Visual Studio.
 
## Description
This is a separate branc of a larger project, ACE (Advanced Computer Engineering). This branch of the project involves developing code in order to allow any one user to control a robotic arm remotely as if it was in a robotic colony in Mars. The arm is intended to rotate left and right, rise up and down and adapt to grab and place, for instance, rocks and other objects into a deposit or storage working together with a rover styled remotely controlled car that was developed in another branch. 
The program was made with different programming languages in order to demonstrate and create versatility and flexibility. 

## Visuals
Images of the robot arms's physical aspects.  
![image](https://user-images.githubusercontent.com/75034234/112049476-972a4200-8b47-11eb-8432-dd973a52a212.png)

## Usage
The Arm has a claw at the tip that can grab things as well as let them go, it can also move according to the needs of the user to redirect the claw in any direction.  
  
## Arm Control
### Python

In order to control the Arm a lot of commands are going to be necessary in this case a keyboard will be enough to do all the commands. The keys to press with be:  
Z / X - clockwise base rotation / counter clockwise base rotation;
R / F - close grips(claw) / open grips;
A / Q - shoulder down / shoulder up;
S / W - elbow down / elbow up;
D / E - wrist down / wrist up;
P - turning LEDs on; 
V - end the program.

Example of the code:

    >>> K_z: usb_arm.BaseClockWise
        
### C++
The keys used to control the Arm in this language are slightly different but with the same end result however, there is the addition of keys to stop the movement. 
; / k - clockwise base rotation / counter clockwise base rotation;
p / i - close grips(claw) / open grips; 
r / v - shoulder down / shoulder up;
e / c - elbow down / elbow up;
w / x - wrist down / wrist up;
  - turning LEDs on; 
o - stops grips; l - stops base; s - stops wrist; d - stops elbow; f - stops shoulder;
q - end the program.

Example of code:

    >>> case 'w': roboarm.setWrist(RobotArm::ARM_UP); break;
## Running the program
The following link leads to a playlist with videos of the testing done:
> https://www.youtube.com/playlist?list=PLRJhhBaK3Fbt_bFId93iR54_QFgr3yZOt

