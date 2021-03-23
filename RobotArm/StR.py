import usb_arm
arm = usb_arm.Arm()
grabStorage = [[usb_arm.BaseCtrClockWise,6.5],[usb_arm.ElbowDown,1.5],[usb_arm.WristDown,.5],[usb_arm.GripsClose],[usb_arm.ElbowUp,1.7],[usb_arm.WristUp, .6]]
arm.doActions(grabStorage)
reset = [[usb_arm.BaseClockWise,6.8],[usb_arm.GripsOpen]]
arm.doActions(reset)
