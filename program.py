import RPi.GPIO as GPIO
import time
#GPIO SETUP
channel=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel,GPIO.IN)
def callback (channel):
	if GPIO.input(channel):
		print ("no water detected")
		else:
print("water detected")
GPIO.add__event_detect(channel, GPIO.BOTH,bouncetime=300)
while true:
 time.sleep(1)
