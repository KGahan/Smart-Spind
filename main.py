#from fingerprint import initSaveFingerprint
import RPi.GPIO as GPIO

def button_callback(channel):
    print("Button was pushed!")

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    print("nothing")
    GPIO.add_event_detect(20,GPIO.BOTH,callback=button_callback)
    print("nix")

setup()
GPIO.output(21,False)

try:  
    while True : pass  
except:
    GPIO.cleanup()