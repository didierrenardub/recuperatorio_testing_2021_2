from ..joystick import ActionPrintText

p = print('d')
p3 =print('')

def test_perform():
    apt = ActionPrintText(2,'vaca','d')
    assert apt.perform(2,'vaca','d') == True 
    apt = ActionPrintText(3,'casa','')
    assert apt.perform(3,'casa',' ') == True 










