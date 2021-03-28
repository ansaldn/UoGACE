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

## Visuals
Images of the robot arms's physical aspects.  
![image](https://user-images.githubusercontent.com/75034234/112049476-972a4200-8b47-11eb-8432-dd973a52a212.png)

## Usage
The Arm has a claw at the tip that can grab things as well as let them go, it can also move according to the needs of the user to redirect the claw in any direction.  
  
## Arm Control
        ´´´K_z: usb_arm.BaseClockWise, 
        K_x: usb_arm.BaseCtrClockWise,
        K_r: usb_arm.CloseGrips,
        K_f: usb_arm.OpenGrips,
        K_a: usb_arm.ShoulderDown,
        K_q: usb_arm.ShoulderUp,
        K_s: usb_arm.ElbowDown,
        K_w: usb_arm.ElbowUp,
        K_d: usb_arm.WristDown,
        K_e: usb_arm.WristUp,
        K_p: usb_arm.LedOn,
        K_v: usb_arm.Stop´´´ 
        
## Running the program
The following link leads to a playlist with videos of the testing done:
> https://www.youtube.com/playlist?list=PLRJhhBaK3Fbt_bFId93iR54_QFgr3yZOt

## Contributing

## Authors and Acknowledgment

## License
