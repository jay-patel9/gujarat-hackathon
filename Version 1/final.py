import os
import time
import RPi.GPIO as GPIO
from example_search import positionNumber
from Read import func
import pyttsx

a = []
a.append(func())
hex = a[0][0]
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.output(20, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)


if hex == 527551543698 and positionNumber == 4:
    LED3 = 18
    GPIO.setup(LED3, GPIO.OUT)
    GPIO.output(LED3,True) 
    time.sleep(2)  
    GPIO.output(LED3,False)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    time.sleep(30)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)
    


elif hex == 4142866182 and positionNumber == 8:
    LED3 = 18
    GPIO.setup(LED3, GPIO.OUT)
    GPIO.output(LED3,True) 
    time.sleep(2)  
    GPIO.output(LED3,False)
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    time.sleep(30)
    GPIO.output(21, GPIO.HIGH)
    GPIO.output(20, GPIO.HIGH)

else:
    engine = pyttsx.init()
    engine.say("Wrong Person")
    engine.runAndWait()
    engine.stop()
    print("Wrong Person")
    LED1 = 22 
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1, GPIO.OUT)
    GPIO.output(LED1,True) 
    time.sleep(2)
    GPIO.output(LED1,False)
    exit(0)
    
