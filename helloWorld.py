from lx16a import *
from math import sin, cos
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize("/dev/ttyUSB0")

# Initializing Servo
print('Initializing servos...')
#servo10 = LX16A(0)
#servo11 = LX16A(11)
#servo12 = LX16A(12)
#servo13 = LX16A(13)
#servo20 = LX16A(20)
#servo21 = LX16A(21)
#servo22 = LX16A(22)
#servo23 = LX16A(23)
servo = [LX16A(10),LX16A(11),LX16A(12),LX16A(13),LX16A(20),LX16A(21),LX16A(22),LX16A(23)]
print('Servos ready')
t=0
while True:
	servo[0].moveTimeWrite(90-90*cos(t))
	pos=servo[0].moveTimeRead()
	t=t+0.01
	print(pos)
#for i in range(0,8):
#	servo[i].loadOrUnloadWrite(0)
#print('Servos disabled')
#while True:
	# Two sine waves out of phase
	# The servos can rotate between 0 and 240 degrees,
	# So we adjust the waves to be in that range
	#servo1.moveTimeWrite(240)
	#servo2.moveTimeWrite(240)
	#servo3.moveTimeWrite(120+30*sin(t)) #min 75, max 165, neutral 120,+-45
	#print(t)
	
	#t += 0.010
