from gpiozero import Button
from signal import pause

def buttonOne():
    print("Hello!")

def buttonTwo():
    print("Goodbye!")

button1 = Button(26)
button2 = Button(19)

button1.when_pressed = buttonOne
button2.when_pressed = buttonTwo

pause()
