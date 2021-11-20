from lx16a import *
from math import sin, cos, pi
import math
import time
import RPi.GPIO as GPIO
import numpy as np


#Created by Xingsheng Wei for driving LarvaBot
#https://github.com/XingshengWei233/LarvaBot.git

#PyLX16-A library reference: https://github.com/ethanlipson/PyLX-16A

#LED red: Initialization started
#LED yellow: Initialization done
#LED light Blue: Homing

#Initialize
print('Initializing...')

# initializing LED
print('Initializing LED...')
red = 18
green = 23
blue = 24
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(red,GPIO.OUT)
GPIO.setup(green,GPIO.OUT)
GPIO.setup(blue,GPIO.OUT)
#set LED off at beginning
GPIO.output(red,GPIO.LOW)
GPIO.output(green,GPIO.LOW)
GPIO.output(blue,GPIO.LOW)
# LED show red
GPIO.output(red,GPIO.HIGH)
print('LED ready')

print('Initializing servo driver...')
# On Raspbian, try each port in /dev/
#LX16A.initialize("/dev/ttyUSB0")
LX16A.initialize("/dev/ttyUSB0")
print('Servo driver ready')

# Initializing Servo
print('Initializing servos...')
servo = [LX16A(10),LX16A(11),LX16A(12),LX16A(13),LX16A(20),LX16A(21),LX16A(22),LX16A(23)]
print('Servos ready')

#initializing parameters
print('Initializing parameters...')
nMotor = 8
homePos = [1, 240, 0, 120, 0, 240, 0, 130]
homeThresh = 1
print('Parameters ready')

# LED show yellow for 1 sec
GPIO.output(red,GPIO.HIGH)
GPIO.output(green,GPIO.HIGH)
print('Initializing Done')
#initializing done

def readPos():
	pos = []
	for i in range(0,nMotor):
		physicalPos = servo[i].getPhysicalPos()
		if physicalPos >360:
			physicalPos = 0
		pos.append(physicalPos)
	return pos

def readCommandedPos():
	pos = []
	for i in range(0,nMotor):
		physicalPos = servo[i].moveTimeRead()
		if physicalPos >360:
			physicalPos = 0
		pos.append(physicalPos)
	return pos

#Auto Homing
def autoHome():
	print('Read Position')
	pos = readPos()
	print('Position before homing:');print(pos)

	GPIO.output(red,GPIO.LOW)
	GPIO.output(green,GPIO.HIGH)
	GPIO.output(blue,GPIO.HIGH)

	homingCount = 0
	homed = False
	while homed == False:
		homed = True
		for i in range(0,nMotor):
			if (abs(pos[i]-homePos[i])>homeThresh):
				pos[i] = pos[i] - 0.5*(pos[i]-homePos[i])/abs(pos[i]-homePos[i])
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
	GPIO.output(red,GPIO.HIGH)
	GPIO.output(green,GPIO.HIGH)
	GPIO.output(blue,GPIO.LOW)
	print('Homing Done')
	#print('Homed Position:');print(pos)

shrink = 90
nod = 30
omega = 3
stepLen = 0.01

def goForward(duration):
	t = 0
	while t<duration:
		servo[0].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[1].moveTimeWrite(240-(shrink-shrink*cos(omega*t)))#240 is loose
		servo[2].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[3].moveTimeWrite(120-nod*sin(omega*t))#120 is rest
		servo[4].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[5].moveTimeWrite(240-(shrink-shrink*cos(omega*t)))#240 is loose
		servo[6].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[7].moveTimeWrite(130-nod*sin(omega*t))#130 is rest
		time.sleep(stepLen)  #0.01
		t += stepLen #0.01
		
def goBackward(duration):
	t = 0
	while t<duration:
		servo[0].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[1].moveTimeWrite(240-(shrink-shrink*cos(omega*t)))#240 is loose
		servo[2].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[3].moveTimeWrite(120+nod*sin(omega*t))#120 is rest
		servo[4].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[5].moveTimeWrite(240-(shrink-shrink*cos(omega*t)))#240 is loose
		servo[6].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[7].moveTimeWrite(130+nod*sin(omega*t))#130 is rest
		time.sleep(stepLen)
		t += stepLen #0.01

def dance(duration):
	t = 0
	upHead = 0
	while t<duration:
		upHead = upHead+0.5
		servo[0].moveTimeWrite(upHead)#0 is loose
		if t>math.pi/omega:
			servo[1].moveTimeWrite(240-(shrink-shrink*cos(omega*t+math.pi)))#240 is loose
		servo[2].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[3].moveTimeWrite(120-0.3*nod*sin(2*omega*t))#120 is rest
		if upHead>=170:
			upHead = 170
		time.sleep(stepLen)
		t += stepLen #0.01

def turnLeft(duration):
	t = 0
	while t<duration:
		servo[0].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[1].moveTimeWrite(240-(shrink-shrink*cos(omega*t)))#240 is loose
		servo[3].moveTimeWrite(120-nod*sin(omega*t))#120 is rest
		servo[4].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[6].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[7].moveTimeWrite(130-nod*sin(omega*t))#130 is rest
		time.sleep(stepLen)
		t += stepLen #0.01

def turnRight(duration):
	t = 0
	while t<duration:
		servo[0].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[2].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[3].moveTimeWrite(120-nod*sin(omega*t))#120 is rest
		servo[4].moveTimeWrite(shrink-shrink*cos(omega*t))#0 is loose
		servo[5].moveTimeWrite(240-(shrink-shrink*cos(omega*t)))#240 is loose
		servo[7].moveTimeWrite(130-nod*sin(omega*t))#130 is rest
		time.sleep(stepLen)
		t += stepLen #0.01

def rest():
	autoHome()
	print('Exited')
	exit()

while True:
	autoHome()
	print('Enter motion (goForward,goBackward,turnLeft,turnRight,dance,rest):')
	motion = input()
	while motion!='goForward' and motion!='goBackward' and motion!='turnLeft' and motion!='turnRight' and motion!='dance' and motion!='rest':
		print('Not valid motion, try again:')
		motion = input()
	if motion == 'rest':
		rest()
		
	print('Enter duration (interger):')
	duration = 'aString'
	while duration.isnumeric() == False:
		duration = input()
		if duration.isnumeric() == False:
			print('Not a number, try again:')
	duration = int(duration)

	if motion == 'goForward':
		goForward(duration)
	if motion == 'goBackward':
		goBackward(duration)
	if motion == 'turnLeft':
		turnLeft(duration)
	if motion == 'turnRight':
		turnRight(duration)
	if motion == 'dance':
		dance(duration)