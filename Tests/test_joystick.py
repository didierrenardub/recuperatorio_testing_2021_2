from ..joystick import Action, Printer, ActionPrintText
from pytest import raises


def test_action_init_id():
    a1 = Action(1)
    assert a1.id() == 1
    a2 = Action(1.5)
    assert a2.id() == ""
    a3 = Action(None)
    assert a3.id() == None
    a4 = Action()
    assert a4.id() == ""
    a5 = Action(123456789)
    assert a5.id() == 12345678
    a6 = Action(-5)
    assert a6.id() == -5
    a7 = Action(" ")
    assert a7.id()== ""


def test_action_perform():
    a = Action(1)
    with raises(NotImplementedError):
        a.perform()


def test_printer():
    p = Printer()
    with raises(NotImplementedError):
        print("Algo")


