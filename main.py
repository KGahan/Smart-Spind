from gpiozero import Button

button = Button(17)

def button_callback():
    print("Button was pushed!")

state = False

while True:
    input = button.is_pressed
    if state == False and input == True:
        state = True
        button_callback()
    if state == True and input == False:
        state = False
