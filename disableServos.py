from lx16a import *
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize("/dev/ttyUSB0")

# Initializing Servo
print('Initializing servos...')
servo = [LX16A(10),LX16A(11),LX16A(12),LX16A(13),LX16A(20),LX16A(21),LX16A(22),LX16A(23)]
print('Servos ready')

homePos = [1, 240, 0, 120, 0, 240, 0, 130]
nMotor = 8
homeThresh = 1

#Auto Homing
print('Read Initial Position')
pos = []
for i in range(0,nMotor):
    physicalPos = servo[i].getPhysicalPos()
    if physicalPos >360:
        physicalPos = 0
    pos.append(physicalPos)
    servo[4].moveTimeWrite(0)
print('Initial Position:');print(pos)

homingCount = 0
homed = False
while homed == False:
	homed = True
	for i in range(0,nMotor):
		if (abs(pos[i]-homePos[i])>homeThresh):
			pos[i] = pos[i] - 0.1*(pos[i]-homePos[i])/abs(pos[i]-homePos[i])
			servo[i].moveTimeWrite(pos[i])
			if pos[i] > 360:
				pos[i]=0
			homed = False
	#print('Current Position:');print(pos)
	time.sleep(0.01)
	if homingCount > 1000:
		print('error: unable to home')
		break
	homingCount = homingCount + 1
print('Homing Done')
#print('Homed Position:');print(pos)

for i in range(0,8):
	servo[i].loadOrUnloadWrite(0)
print('Servos disabled')

while True:
    pos = []
    for i in range(0,8):
        physicalPos = servo[i].getPhysicalPos()
        if physicalPos >360:
            physicalPos = 0
        pos.append(physicalPos)
        servo[4].moveTimeWrite(0)
    print('Position:');print(pos)

