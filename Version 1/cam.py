import picamera
import time

camera = picamera.PiCamera()
camera.start_preview()

for i in range(0,1):
	time.sleep(0.5)
	camera.vflip = True
	camera.capture(str(i+1)+".jpg")
	camera.stop_preview()


