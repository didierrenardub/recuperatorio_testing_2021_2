from ..joystick import Button

def test_button_invalid_label():
    invalid = [
        None,
        True,
        0.123, 
        345
    ]
    for test_label, expected_output in invalid.items():
        assert Button(test_label) == expected_output

def test_button_label():
    b1 = Button()
    assert b1.label() == ''
    b2 = Button('Vicky')
    assert b2.label() == 'Vicky'
    b3 = Button('Vicky Baral')
    assert b3.label() == 'Vicky Baral'
    b4 = Button(None)
    assert b4.label() == ''

def test_button_press():
    b = Button()
    assert b.perform(b) == True
    assert b.label('v') == True and b.press() == True
    assert b.label(-1) == False and b.press() == False
    assert b.label(None) == True and b.press() == True
    

