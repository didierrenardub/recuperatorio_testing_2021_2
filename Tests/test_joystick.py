from ..joystick import Action, Printer, ActionPrintText, Button, Joystick
from pytest import raises


def test_action_init_id():
    a1 = Action(1)
    assert a1.id() == 1
    a2 = Action(1.5)
    assert a2.id() == 1
    a3 = Action(None)
    assert a3.id() == 0
    a4 = Action()
    assert a4.id() == 0
    a5 = Action(2)
    assert a5.id() == 2
    a6 = Action(-5)
    assert a6.id() == 5
    a7 = Action(10000)
    assert a7.id() == 10000
    a8 = Action(10001)
    assert a8.id() == 10000



def test_action_perform():
    a = Action(1)
    with raises(NotImplementedError):
        a.perform()


def test_printer():
    p = Printer()
    with raises(NotImplementedError):
        p.print("Chayanne")


def test_ActionPrintText_init():
    printer = Printer()
    apt1 = ActionPrintText(1, "texto", printer)
    assert apt1._text == "texto" and apt1._printer == printer
    apt2 = ActionPrintText(1, "", printer)
    assert apt2._text == "" and apt2._printer == printer
    apt3 = ActionPrintText(1, None, printer)
    assert apt3._text == "" and apt3._printer == printer
    apt4 = ActionPrintText(1, "texto", None)
    assert apt4._text == "texto" and apt4._printer is None


def test_Button_init():
    b1 = Button("hola")
    assert b1.label() == "hola" and b1._action is None
    printer = Printer()
    apt1 = ActionPrintText(1, "texto", printer)
    b2 = Button("hola", apt1)
    assert b2.label() == "hola" and b2._action is not None
    b3 = Button(None, apt1)
    assert b3.label() == "" and b3._action is not None

def test_Button_press():
    printer = Printer()
    apt1 = ActionPrintText(1, "texto", printer)
    b1 = Button("hola", apt1)
    assert b1.press() == True
    b2 = Button("hola")
    assert b2.press() == False


def test_Joystick_init():
    j1 = Joystick()
    assert j1._buttons == []

def test_Joystick_add_button():
    j1 = Joystick()
    b = Button("Hola")
    assert j1.add_button(b) == True
    assert j1._button == [b]