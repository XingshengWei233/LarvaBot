from lx16a import *
from math import sin, cos
import time
import RPi.GPIO as GPIO
import numpy as np

print('Initializing...')
# initializing LED
red = 18
green = 23
blue = 24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
# LED show red
GPIO.output(red,GPIO.HIGH)
print('Initializing Done')
# On Raspbian, try each port in /dev/
#LX16A.initialize("/dev/ttyUSB0")
LX16A.initialize("/dev/ttyUSB0")
# Initializing Servo
#servo10 = LX16A(10)
#servo11 = LX16A(11)
#servo12 = LX16A(12)
#servo13 = LX16A(13)
#servo20 = LX16A(20)
#servo21 = LX16A(21)
#servo22 = LX16A(22)
#servo23 = LX16A(23)
servo = [LX16A(10),LX16A(11),LX16A(12),LX16A(13),LX16A(20),LX16A(21),LX16A(22),LX16A(23)]
#initializing parameters
nMotor = 8
#homePos = 
# LED show yellow for 1 sec
GPIO.output(red,GPIO.HIGH)
GPIO.output(green,GPIO.HIGH)
print('Initializing Done')
#initializing done

#Auto Checking 

#Auto Homing
print('Read Initial Position')
pos = []
for i in range(0,nMotor):
	pos.append(servo[i].moveTimeRead())
print('Initial Position:');print(pos)
#while




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
