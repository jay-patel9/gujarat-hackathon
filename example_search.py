#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
PyFingerprint
Copyright (C) 2015 Bastian Raschke <bastian.raschke@posteo.de>
All rights reserved.

"""
import RPi.GPIO as GPIO
import time
import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
import pyttsx

## Search for a finger
##

## Tries to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyUSB0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

## Gets some sensor information
print('Currently used templates: ' + str(f.getTemplateCount()) +'/'+ str(f.getStorageCapacity()))

## Tries to search the finger and calculate hash
try:
    engine = pyttsx.init()
    engine.say("Waiting for finger")
    engine.runAndWait()
    engine.stop()
    print('Waiting for finger...')

    ## Wait that finger is read
    while ( f.readImage() == False ):
        pass

    ## Converts read image to characteristics and stores it in charbuffer 1
    f.convertImage(0x01)

    ## Searchs template
    result = f.searchTemplate()

    positionNumber = result[0]
    accuracyScore = result[1]

    if ( positionNumber == -1 ):
        engine = pyttsx.init()
        engine.say("No match found")
        engine.runAndWait()
        engine.stop()
        print('No match found!')
	LED1 = 22 
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED1, GPIO.OUT)
	GPIO.output(LED1,True) 
        time.sleep(2)
	GPIO.output(LED1,False)
	exit(0)
    else:
        print(str(positionNumber))
        LED2 = 14 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED2, GPIO.OUT)
        GPIO.output(LED2,True) 
        time.sleep(2)
	GPIO.output(LED2,False)

	#print('The accuracy score is: ' + str(accuracyScore))

    ## OPTIONAL stuff
    ##

    ## Loads the found template to charbuffer 1
    f.loadTemplate(positionNumber, 0x01)

    ## Downloads the characteristics of template loaded in charbuffer 1
    characterics = str(f.downloadCharacteristics(0x01)).encode('utf-8')

    ## Hashes characteristics of template
    #print('SHA-2 hash of template: ' + hashlib.sha256(characterics).hexdigest())

except Exception as e:
    print('Operation failed!')
    print('Exception message: ' + str(e))
    exit(1)
