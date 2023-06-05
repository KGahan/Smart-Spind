import RPi.GPIO as GPIO
import time
port1 = 18
port2 = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(port1,GPIO.OUT)
GPIO.setup(port2,GPIO.OUT)
GPIO.output(port1,False)
GPIO.output(port2,False)

def openSchloss(spindId):
    if spindId == 1:
        openAndClose(port1)
    elif spindId == 2:
        openAndClose(port2)
        
def openAndClose(port):
    GPIO.output(port, True)
    time.sleep(2)
    GPIO.output(port,False)