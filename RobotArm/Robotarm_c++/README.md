# README

### The program allows the user to control the OWI-535 ROBOTIC ARM using a keyboard connected to the raspberry pi

The official USB interface module of the robot arm works only in windows and do not provide API.  To compile and run these files written in c++. We installed:

`sudo apt-get install build-essential` which includes the GCC/g++ compilers and some libraries used in this program.

`sudo apt-get install libusb-dev` this is the libusb, a C library that provides access to USB devices on Linux.

`sudo apt-get install ncurses-dev` the ncurses library which is used to capture keyboard input.

To download the code type: `Git clone github.com/da5905p/UoGACE/RobotArm/Robotarm_c++`

Go to `cd robotarm_c++` and compile the code using `make`

Finally, to run the program and control the robot arm with the keyboard, type:  `sudo ./robot`

This project is based on the research posted on (https://notbrainsurgery.livejournal.com/38622.html)
