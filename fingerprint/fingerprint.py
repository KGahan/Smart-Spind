import time
import serial

import adafruit_fingerprint

uart = serial.Serial("/dev/ttyS0", baudrate=57600, timeout=1)
finger = adafruit_fingerprint.Adafruit_Fingerprint(uart)

def initSaveFingerprint(spindId):
    print("init")
    check_functionality()
    get_fingerprint()
    templateFingerprint()
    saveFingerprint(spindId)
    return True

def initCheckFingerprint(spindId):
    print("checkFinger")
    check_functionality()
    while finger.get_image() != adafruit_fingerprint.OK:
        pass
    if finger.image_2_tz(1) != adafruit_fingerprint.OK:
        return False
    if finger.finger_search() != adafruit_fingerprint.OK:
        return False
    if finger.finger_id == spindId:
        print("found", finger.confidence)
        return True
    else:
        return False

def check_functionality():
    if finger.read_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    if finger.count_templates() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to read templates")
    if finger.read_sysparam() != adafruit_fingerprint.OK:
        raise RuntimeError("Failed to get system parameters")
    print("check")

def get_fingerprint():
    fingerImage = finger.get_image()
    if fingerImage == adafruit_fingerprint.NOFINGER:
        get_fingerprint()
    if fingerImage == adafruit_fingerprint.OK:
        print("get")
        return True
    elif fingerImage == adafruit_fingerprint.IMAGEFAIL:
        return False
    else:
        return False

def templateFingerprint():
    print("template")
    finger.image_2_tz(1)

def saveFingerprint(location):
    finger.create_model()
    finger.store_model(location)
    print("save")
