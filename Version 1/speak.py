import pyttsx
##from subprocess import call

##speech="marvin"
##call(["espeak", speech])

engine = pyttsx.init()
engine.say("enter licence card")
engine.runAndWait()
engine.stop()
