#Robot to Storage script
#Created by Goncalo
#Version 1.0

import usb_arm
arm = usb_arm.Arm()

grabForward = [[usb_arm.ElbowDown,2],[usb_arm.WristDown, .5],[usb_arm.GripsClose],[usb_arm.ElbowUp,2.2],[usb_arm.WristUp,.6]]
arm.doActions(grabForward)

rotate = [[usb_arm.BaseCtrClockWise,7],[usb_arm.GripsOpen],[usb_arm.BaseClockWise,6.8]]
arm.doActions(rotate)
