# Initialize the EV3 Brick.
ev3 = EV3Brick() # type: ignore
# Initialize the motors.
left_motor = Motor(Port.B) # type: ignore
right_motor = Motor(Port.C) # type: ignore
# Initialize the sensors.
colorSensor = PybricksColorSensor(Port.S1) # type: ignore
# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104) # type: ignore
# Set the Drive Speed.
DRIVE_SPEED = 100
# Go forward and backwards for one meter.
robot.straight(1000)
ev3.speaker.beep()
robot.straight(-1000) and ev3.speaker.beep()