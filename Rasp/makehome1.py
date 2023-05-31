import RPi.GPIO as GPIO

import time

servoPIN = 11
Switch1= 10
Switch2= 16
Red= 15
Green= 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(Switch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(Switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Green, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

flag = False



try:
	while True:
		
		if GPIO.input(Switch1) == GPIO.HIGH :
			p.ChangeDutyCycle(10)
			time.sleep(3.0)
			p.ChangeDutyCycle(2.5)
		if GPIO.input(Switch2) == GPIO.HIGH and flag == False:
			GPIO.output(Green, GPIO.HIGH)
			GPIO.output(Red, GPIO.HIGH)
			flag = True
		if GPIO.input(Switch2) == GPIO.HIGH and flag == True:
			GPIO.output(Green, GPIO.LOW)
			GPIO.output(Red, GPIO.LOW)
			flag = False

			
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()
