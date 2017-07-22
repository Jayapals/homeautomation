import RPi.GPIO as GPIO
import time




		# Numbers GPIOs by physical location
	GPIO.setup(21, GPIO.OUT)	# Set pins' mode is output
	global Buzz						# Assign a global variable to replace GPIO.PWM 
	Buzz = GPIO.PWM(21, 440)	# 440 is initial frequency.
	Buzz.start(50)					# Start Buzzer pin with 50% duty ration


