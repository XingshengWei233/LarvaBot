from lx16a import *
from math import sin, cos
import time

print('Running')
# This is the port that the controller board is connected to
# This will be different for different computers
# On Windows, try the ports COM1, COM2, COM3, etc...
# On Raspbian, try each port in /dev/
#LX16A.initialize("/dev/ttyUSB0")
LX16A.initialize("/dev/ttyUSB0")
# There should two servos connected, with IDs 1 and 2
servo10 = LX16A(10)
#servo11 = LX16A(11)
#servo12 = LX16A(12)
#servo13 = LX16A(13)
servo20 = LX16A(20)
t = 0

#def initialPos():
#	pos11 = servo11.moveTimeRead()


#def limit():

while True:
	# Two sine waves out of phase
	# The servos can rotate between 0 and 240 degrees,
	# So we adjust the waves to be in that range
	servo10.moveTimeWrite(0)#0 is loose, 120 is tight
	pos10=servo10.moveTimeRead()
	#servo11.moveTimeWrite(240) #240 is loose
	#pos11=servo11.moveTimeRead()
	#servo12.moveTimeWrite(0) #0 is loose
	#pos12=servo12.moveTimeRead()
	#servo13.moveTimeWrite(120) #min 75, max 165, neutral 120,+-45
	servo20.moveTimeWrite(0)#0 is loose, 120 is tight
	pos20=servo20.moveTimeRead()
	print(pos10)
	print(pos20)
	print('running')
	
	t += 0.01
