import RPi.GPIO as GPIO
import time
port = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(port,GPIO.OUT)

def openSchloss():
    GPIO.output(port, True)
    time.sleep(1)
    GPIO.output(port,False)