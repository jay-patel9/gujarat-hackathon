import os
import time
import RPi.GPIO as GPIO
from example_search import positionNumber
from Read import func

a = []
a.append(func())
hex = a[0][0]

if hex == 527551543698 and positionNumber == 4:
    LED3 = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED3, GPIO.OUT)
    GPIO.output(LED3,True) 
    time.sleep(2)  
    GPIO.output(LED3,False)

    f = open('sample.txt', 'w')
    f.write(str(hex))
    f.close()
    
    os.system('python cam.py')
    time.sleep(1)
    os.system('python client.py 1')
    
    # wait for sweta to provide response
    time.sleep(10)
    os.system('python res.py')

elif hex == 4142866182 and positionNumber == 8:
    LED3 = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED3, GPIO.OUT)
    GPIO.output(LED3,True) 
    time.sleep(2)  
    GPIO.output(LED3,False)

    f = open('sample.txt', 'w')
    f.write(str(hex))
    f.close()
    os.system('python cam.py')
    time.sleep(1)
    os.system('python client.py 1')
    
    # wait for sweta to provide response
    time.sleep(5)
    os.system('python res.py')
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
    
