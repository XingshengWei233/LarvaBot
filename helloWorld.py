from lx16a import *
from math import sin, cos
import time

# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
LX16A.initialize("/dev/ttyUSB0")

# There should two servos connected, with IDs 1 and 2
servo1 = LX16A(21)
servo2 = LX16A(22)
servo3 = LX16A(23)
print('s')
t = 0

while True:
	# Two sine waves out of phase
	# The servos can rotate between 0 and 240 degrees,
	# So we adjust the waves to be in that range
	#servo1.moveTimeWrite(240)
	#servo2.moveTimeWrite(240)
	#servo3.moveTimeWrite(120+30*sin(t)) #min 75, max 165, neutral 120,+-45
	print(t)
	
	t += 0.010
