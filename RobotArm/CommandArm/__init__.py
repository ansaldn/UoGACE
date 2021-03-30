"""Maplin USB Robot arm control.
Usage - 
>>> import usb_arm
>>> arm = usb_arm.Arm()
>>> arm.move(usb_arm.OpenGrips)
>>> arm.doActions(block_left) # WARNING - ARM SHOULD BE ALL THE WAY RIGHT BEFORE TRYING THIS

Trouble:
"NO back end found" - you need to install a libusb driver on your system.
"""

#lisusb library
import usb.core
from time import sleep


class BitPattern(object):
    """A bit pattern to send to a robot arm"""
    __slots__ = ['arm', 'base', 'led']

#arm,base,led slots
    def __init__(self, arm, base, led):
        self.arm = arm
        self.base = base
        self.led = led
	
#initializing the slots
    def __iter__(self):
        return iter([self.arm, self.base, self.led])

#time command
    def __getitem__(self, item):
        return [self.arm, self.base, self.led][item]

#more than 1 command
    def __or__(self, other):
        return BitPattern(self.arm | other.arm,
                          self.base | other.base,
                          self.led | other.led)

#bit table
#1,2 grip
#4,8 Wrist
#10,20 Elbow
#40, 80 Shoulder
#0,1 0,2 baseclock

GripsClose =       BitPattern(1, 0, 0) 
GripsOpen =        BitPattern(2, 0, 0) 
Stop =             BitPattern(0, 0, 0)
WristUp =          BitPattern(0x4, 0, 0)
WristDown =        BitPattern(0x8, 0, 0)
ElbowUp =          BitPattern(0x10, 0, 0)
ElbowDown =        BitPattern(0x20, 0, 0)
ShoulderUp =       BitPattern(0x40, 0, 0)
ShoulderDown =     BitPattern(0x80, 0, 0)
BaseClockWise =    BitPattern(0, 1, 0)
BaseCtrClockWise = BitPattern(0, 2, 0)
LedOn =            BitPattern(0, 0, 1)


class Arm(object):
    """Arm interface"""
    __slots__ = ['dev']

    def __init__(self):
        self.dev = usb.core.find(idVendor=0x1267) #usb library
        self.dev.set_configuration()

    def tell(self, msg):
        """Send a USB messaqe to the arm"""
        self.dev.ctrl_transfer(0x40, 6, 0x100, 0, msg)
	
#exception stop
    def safe_tell(self, fn):
        """Send a message to the arm, with a stop
        to ensure that the robot stops in the
        case of an exception"""
        try:
            fn()
        except:
            self.tell(Stop)
            raise
#move function with bitpattern and time
    def move(self, pattern, time=1):
        """Perform a pattern move with timing and stop"""
        try:
        	self.tell(pattern)
        	sleep(time)
        finally:
        	self.tell(Stop)
		
#functions for outside script usage
    def doActions(self, actions):
        """Params: List of actions - each is a list/tuple of BitPattern and time
         (defaulting to 1 if not set)"""
        #Validate
        for action in actions:
            if not 1 <= len(action) <= 2:
                raise ValueError("Wrong number of parameters in action %s" %
                                 (repr(action)))
            if not isinstance(action[0], BitPattern):
                raise ValueError("Not a valid action")
        #Do
        for action in actions:
            if len(action) == 2:
                time = action[1]
            else:
                time = 1
            self.move(action[0], time)

#basic built in movement
def makeGrabAndMove(baseDir):
	return [[CloseGrips, 1.1],
                [ShoulderUp | ElbowUp | WristDown | baseDir],
                [baseDir, 8.5],
                [ShoulderDown | ElbowDown | WristUp | baseDir],
                [OpenGrips]]

#move basic movement
blink = [[LedOn, 0.5], [Stop, 0.5]] * 3
block_left = makeGrabAndMove(BaseClockWise) + blink
block_right = makeGrabAndMove(BaseCtrClockWise) + blink
