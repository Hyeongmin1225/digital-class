import RPi.GPIO as GPIO 
import time

Switch1= 10
Switch2= 16
Switch3= 18
Red= 11
Green= 13
Blue= 15

GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BOARD) 

GPIO.setup(Switch1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.setup(Switch2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Switch3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(Red, GPIO.OUT)
GPIO.setup(Green, GPIO.OUT)
GPIO.setup(Blue, GPIO.OUT)


while True: 
    if GPIO.input(Switch1) == GPIO.HIGH:
        print("Button1 was pushed!")
        GPIO.output(Red, GPIO.HIGH)
    elif GPIO.input(Switch2) == GPIO.HIGH:
        print("Button2 was not pushed!")  
        GPIO.output(Green, GPIO.HIGH) 
    elif GPIO.input(Switch3) == GPIO.HIGH:
        print("Button3 was pushed!")
        GPIO.output(Blue, GPIO.HIGH)
        
    else:
        print("Button1 was not pushed!")
        print("Button2 was not pushed!")
        print("Button3 was not pushed!")
        GPIO.output(Green, GPIO.LOW)  
        GPIO.output(Blue, GPIO.LOW)  
        GPIO.output(Red, GPIO.LOW)   
    time.sleep(0.5)
