from ..joystick import Printer
from py import raises

def test_printer_print():
    p = Printer(" ")
    with raises(NotImplementedError):
        p.print()
    

