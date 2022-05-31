import RPi.GPIO as GPIO
import time
print('start')
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

print ("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(18,GPIO.LOW)

print ("LED on")
GPIO.output(23,GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(23,GPIO.LOW)

print ("LED on")
GPIO.output(24,GPIO.HIGH)
time.sleep(1)
print ("LED off")
GPIO.output(24,GPIO.LOW)

print('end')