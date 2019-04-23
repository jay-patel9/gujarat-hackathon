import RPi.GPIO as GPIO
import SimpleMFRc522

reader = SimpleMFRc522.SimpleMFRc522()

try:
    id = reader.read()
    print(id)
finally:
    GPIO.cleanup()