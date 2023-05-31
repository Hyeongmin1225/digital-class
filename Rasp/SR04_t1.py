import RPi.GPIO as GPIO
import time

PinEcho= 38
PinTrig= 40
Green= 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO. BOARD)
GPIO.setup(Green, GPIO.OUT)
GPIO.setup(PinTrig, GPIO.OUT) 
GPIO.setup(PinEcho, GPIO.IN) 


startTime=0
stopTime=0

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
