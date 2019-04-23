import socket
import sys
import zipfile
import os
import os.path
import time
import RPi.GPIO as GPIO
import pyttsx

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.output(20, GPIO.HIGH)
GPIO.output(21, GPIO.HIGH)

port = 1337

ss = socket.socket()
print('[+] Server socket is created.')

ss.bind(('', port))
print('[+] Socket is binded to {}'.format(port))

ss.listen(5)
print('[+] Waiting for connection...')

con, addr = ss.accept()
print('[+] Got connection from {}'.format(addr[0]))

filename = con.recv(1024).decode()

f = open(filename, 'wb')
l = con.recv(1024)
while(l):
	f.write(l)
	l = con.recv(1024)
f.close()
print('[+] Received file ' + filename)

with zipfile.ZipFile(filename, 'r') as file:
	print('[+] Extracting files...')
	file.extractall()
	print('[+] Done')

	
##if ans == "true":


os.remove(filename)
con.close()
ss.close()

path1 = '1.txt'
path2 = '2.txt'

if os.path.isfile(path1):
    LED4 = 27
    GPIO.setup(LED4, GPIO.OUT)
    GPIO.output(LED4,True)
    engine = pyttsx.init()
    engine.say("Start Your Vehicle")
    engine.runAndWait()
    engine.stop()
    GPIO.output(20, GPIO.LOW)
    GPIO.output(21, GPIO.LOW)
    time.sleep(15)
    time.sleep(2) 
    GPIO.output(LED4,False)
    os.remove('1.txt')
else:
    pass

if os.path.isfile(path2):
    LED5 = 22
    GPIO.setup(LED5, GPIO.OUT)
    GPIO.output(LED5,True)
    engine = pyttsx.init()
    engine.say("Unauthorized Access")
    engine.say("Message has been sent to the Owner")
    os.system("python3 sms.py")
    engine.runAndWait()
    engine.stop()
    GPIO.output(20, GPIO.HIGH)
    GPIO.output(21, GPIO.HIGH)
    time.sleep(2) 
    GPIO.output(LED5,False)
    os.remove('2.txt')
else:
    pass