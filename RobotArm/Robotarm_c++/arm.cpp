#include "robotarm.h"
void RobotArm::connect() {
	struct usb_bus *busses;
	usb_init();
	usb_find_busses();
	usb_find_devices();
	
	busses = usb_get_busses();
	
	struct usb_bus *bus;
	struct usb_device *arm = NULL;
	for(bus = busses; bus; bus = bus->next) {
		
		struct usb_device *dev;
		for(dev = bus->devices; dev; dev = dev->next) {
			if(dev->descriptor.idVendor == USB_VENDOR && dev->descriptor.idProduct == USB_PRODUCT) {
				arm = dev;
				break;
			} 
		}
	}
	if(arm == NULL) {
		throw "Could not find robot arm";
	}
	
	int result;
	armh = usb_open(arm);
}

RobotArm::RobotArm() {
	commands[0] = commands[1] = commands[2] = 0;
}

// disconnect from robot arm
void RobotArm::disconnect() {
	usb_close(armh);
}

// send the current control bytes to the robot arm
void RobotArm::sendCommand() {
	usb_control_msg(armh, 0x40, 6, 0x100, 0, commands, 3, 0);
}

// set the current control bytes and then send them to the robot arm
void RobotArm::sendCommand(char * commands){
	this->commands[0] = commands[0];
	this->commands[1] = commands[1];
	this->commands[2] = commands[2];
	sendCommand();
}

// stop all motors and turn LED off
void RobotArm::stopAll(){
	commands[0] = commands[1] = commands[2] = 0;
	sendCommand();
}

// set grip to ARM_STOP, ARM_CLOSE or ARM_OPEN
void RobotArm::setGrip(RobotArm::MotorDirection direction) {
	// bits 0 and 1 ('00000011') of byte 0
	switch(direction) {
		case ARM_STOP:
			commands[0] = 0 | (commands[0] & 0xFC);
		break;
		case ARM_CLOSE:
			commands[0] = 0x1 | (commands[0] & 0xFC);
		break;
		case ARM_OPEN:
			commands[0] = 0x2 | (commands[0] & 0xFC);
		break;
	}
	sendCommand();
}

// set wrist to ARM_STOP, ARM_UP or ARM_DOWN
void RobotArm::setWrist(RobotArm::MotorDirection direction) {
	// bits 2 and 3 ('00001100') of byte 0
	switch(direction) {
		case ARM_STOP:
			commands[0] = 0 | (commands[0] & 0xF3);
		break;
		case ARM_UP:
			commands[0] = 0x4 | (commands[0] & 0xF3);
		break;
		case ARM_DOWN:
			commands[0] = 0x8 | (commands[0] & 0xF3);
		break;
	}
	sendCommand();
}

// set elbow to ARM_STOP, ARM_UP or ARM_DOWN
void RobotArm::setElbow(RobotArm::MotorDirection direction) {
	// bits 4 and 5 ('00110000') of byte 0
	switch(direction) {
		case ARM_STOP:
			commands[0] = 0 | (commands[0] & 0xCF);
		break;
		case ARM_UP:
			commands[0] = 0x10 | (commands[0] & 0xCF);
		break;
		case ARM_DOWN:
			commands[0] = 0x20 | (commands[0] & 0xCF);
		break;
	}
	sendCommand();
}

// set shoulder to ARM_STOP, ARM_UP or ARM_DOWN
void RobotArm::setShoulder(RobotArm::MotorDirection direction) {
	// bits 6 and 7 ('11000000') of byte 0
	switch(direction) {
		case ARM_STOP:
			commands[0] = 0 | (commands[0] & 0x3F);
		break;
		case ARM_UP:
			commands[0] = 0x40 | (commands[0] & 0x3F);
		break;
		case ARM_DOWN:
			commands[0] = 0x80 | (commands[0] & 0x3F);
		break;
	}
	sendCommand();
}

// set base to ARM_STOP, ARM_CLOCKWISE or ARM_ANTICLOCKWISE
void RobotArm::setBase(RobotArm::MotorDirection direction) {
	// bits 0 and 1 ('00000011') of byte 1
	switch(direction) {
		case ARM_STOP:
			commands[1] = 0 | (commands[1] & 0xFC);
		break;
		case ARM_CLOCKWISE:
			commands[1] = 0x1 | (commands[1] & 0xFC);
		break;
		case ARM_ANTICLOCKWISE:
			commands[1] = 0x2 | (commands[1] & 0xFC);
		break;
	}
	sendCommand();
}

// set LED to true (on) or false (off)
void RobotArm::setLED(bool on) {
	commands[2] = on? 1 : 0;
	sendCommand();
}
