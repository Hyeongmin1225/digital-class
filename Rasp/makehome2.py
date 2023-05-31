import RPi.GPIO as GPIO
import time

PinEcho= 38
PinTrig= 40
Green= 13
servoPIN = 11
Switch1= 10
Switch2= 16
Red= 15


GPIO.setwarnings(False)
GPIO.setmode(GPIO. BOARD)
GPIO.setup(servoPIN, GPIO.OUT)
GPIO.setup(Switch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(Switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Green, GPIO.OUT)
GPIO.setup(PinTrig, GPIO.OUT) 
GPIO.setup(PinEcho, GPIO.IN) 


startTime=0
stopTime=0

p = GPIO.PWM(servoPIN, 50) # GPIO 17 for PWM with 50Hz
p.start(2.5) # Initialization

flag = False

while True:
	GPIO.output(PinTrig, False) 
	time.sleep(2)
	# trigger
	GPIO.output(PinTrig, True) 
	time.sleep(0.00001) 
	GPIO.output(PinTrig, False) 
	# echo
	while GPIO.input(PinEcho) == 0: 
		startTime = time.time()
	while GPIO.input(PinEcho) == 1: 
		stopTime = time.time()
	Time_interval= stopTime - startTime
	Distance = Time_interval * 17000
	Distance = round(Distance, 1)
	Distance1 = str(Distance)
	length = "Distance " + Distance1 +"cm"
	print (length)	
	if Distance<5 :
		for _ in range(5):
			GPIO.output(Green, GPIO.HIGH)  
			time.sleep(0.3)  
			GPIO.output(Green, GPIO.LOW)  
			time.sleep(0.3)
	if GPIO.input(Switch1) == GPIO.HIGH :
		p.ChangeDutyCycle(10)
		time.sleep(3.0)
		p.ChangeDutyCycle(2.5)
	if GPIO.input(Switch2) == GPIO.HIGH and flag == False:
		GPIO.output(Red, GPIO.HIGH)
		flag = True
	if GPIO.input(Switch2) == GPIO.HIGH and flag == True:
		GPIO.output(Red, GPIO.LOW)
		flag = False
