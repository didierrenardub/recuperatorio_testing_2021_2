from ..joystick import Joystick

button = ['x','w','q','r']
button2 = []


def test_joystick_add_button():
    button.append(button)
    assert button.append(button) == True
    button2.append(button2)
    assert button.append(button2) == False

def test_joystick_press():
    
