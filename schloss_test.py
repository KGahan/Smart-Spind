import RPi.GPIO as GPIO
import time
port = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(port,GPIO.OUT)
time.sleep(1)
GPIO.output(port,False)
print("false")
time.sleep(1)
print("true")

GPIO.output(port, True)
time.sleep(1)
print("false")
GPIO.output(port, False)
time.sleep(1)
print("done")
GPIO.cleanup()
