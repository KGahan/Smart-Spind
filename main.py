from gpiozero import Button
from signal import pause
from fingerprint.fingerprint import initSaveFingerprint, initCheckFingerprint
from facial_recognition.headshots import make_headshots
from facial_recognition.train_model import train_model
from facial_recognition.facial_req import recognize_face
from schloss import openSchloss
from time import sleep
import json

def savedSpind(spindId, method):
    data = getSpindData()
    data["spinds"].append({"id": spindId, "method": method})
    json_opject = json.dumps(data, indent=4)
    with open("spind_data.json", "w") as outfile:
        outfile.write(json_opject)

def finger(spindId):
    if (initSaveFingerprint(spindId)):
        savedSpind(spindId, "fingerprint")
    else:
        print("failed when saving fingerprint")

def face(spindId):
    print("face")
    make_headshots(spindId)
    train_model(spindId)
    print("done")

def finger_or_face(buttonId):
    print(buttonId)
    sleep(0.5)
    while True:
        if button1.is_pressed:
            face(buttonId)
            return
        elif button2.is_pressed:
            finger(buttonId)
            return

def getSpindData():
    with open("spind_data.json", 'r') as openfile:
        return json.load(openfile)

def spindIsSafed(data, spindId):
    if len(list(filter(lambda spind: spind['id'] == spindId, data))) > 0:
        return True
    else:
        return False

def getSpindStatus(spindId):
    data = getSpindData()
    if len(data["spinds"]) == 0 or not spindIsSafed(data["spinds"], spindId):
        finger_or_face(spindId)
    else:
        spindData = list(filter(lambda spind: spind['id'] == spindId, data["spinds"]))[0]
        if spindData["method"] == "fingerprint":
            if initCheckFingerprint(spindId):
                openSchloss()
            else:
                print("not recognized")

def buttonOne():
    getSpindStatus(1)

def buttonTwo():
    getSpindStatus(2)

button1 = Button(26)
button2 = Button(19)

button1.when_pressed = buttonOne
button2.when_pressed = buttonTwo

pause()
