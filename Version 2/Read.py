#!/usr/bin/env python
import pyttsx
import RPi.GPIO as GPIO
import SimpleMFRC522

def func():
	
	reader = SimpleMFRC522.SimpleMFRC522()
	try:
            engine = pyttsx.init()
            engine.say("enter licence card")
            engine.runAndWait()
            engine.stop()
	    print("Enter Licence Card")
            id, text = reader.read()
            return(id, text)
	finally:
        	GPIO.cleanup()
