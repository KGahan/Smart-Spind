import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)

GPIO.output(21,False)
time.sleep(1)
print("1")

GPIO.output(21, True)
time.sleep(1)
print("2")
GPIO.output(21, False)