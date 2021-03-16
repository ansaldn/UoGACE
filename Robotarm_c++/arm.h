#include <usb.h>

#define USB_VENDOR 0x1267
#define USB_PRODUCT 0

class RobotArm {
	protected:
	// handle to usb device 
	usb_dev_handle *armh;
	
	// command bytes
	char commands[3];
	
	/* Byte 1:
	Bit: 		Function:
	0-1			Grip (00 stop, 01 close, 10 open)
	2-3			Wrist (00 stop, 01 up, 10 down)
	4-5			Elbow (00 stop, 01 up, 10 down)
	6-7			Shoulder (00 stop, 01 up, 10 down)
	
	Byte 2: 
	0-1			Base (00 stop, 01 clockwise, 10 anti clockwise)
	
	Byte 3:
	0			LED (0 off, 1 on)
	*/
	
	public:
	
	enum MotorDirection {
		ARM_STOP, ARM_OPEN, ARM_CLOSE, ARM_UP, ARM_DOWN, ARM_CLOCKWISE, ARM_ANTICLOCKWISE
	};
	
	// constructor
	RobotArm();
	
	// connect to robot arm
	void connect();
	
	// disconnect from robot arm
	void disconnect();
	
	// stop all motors and turn LED off
	void stopAll();
	
	// set grip to ARM_STOP, ARM_CLOSE or ARM_OPEN
	void setGrip(MotorDirection direction);
	
	// set wrist to ARM_STOP, ARM_UP or ARM_DOWN
	void setWrist(MotorDirection direction);
	
	// set elbow to ARM_STOP, ARM_UP or ARM_DOWN
	void setElbow(MotorDirection direction);
	
	// set shoulder to ARM_STOP, ARM_UP or ARM_DOWN
	void setShoulder(MotorDirection direction);
	
	// set base to ARM_STOP, ARM_CLOCKWISE or ARM_ANTICLOCKWISE
	void setBase(MotorDirection direction);
	
	// set LED to true (on) or false (off)
	void setLED(bool on);
	
	
	
	// send the current control bytes to the robot arm
	void sendCommand();
	
	// set the current control bytes and then send them to the robot arm
	void sendCommand(char * commands);
	
};
