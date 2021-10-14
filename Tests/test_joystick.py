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
    a5 = Action(2)
    assert a5.id() == 1
    a6 = Action(-5)
    assert a6.id() == -5
    a7 = Action(" ")
    assert a7.id() == ""


def test_action_perform():
    a = Action(1)
    with raises(NotImplementedError):
        a.perform()


def test_printer():
    p = Printer()
    with raises(NotImplementedError):
        print("Chayanne")


def test_ActionPrintText_init():
    printer = Printer()
    apt1 = ActionPrintText(1, "texto", printer)
    assert apt1._text == "texto" and apt1._printer == printer
    apt2 = ActionPrintText(1, "", printer)
    assert apt2._text == "" and apt2._printer == printer
    apt3 = ActionPrintText(1, None, printer)
    assert apt3._text == "" and apt3._printer == printer
    apt4 = ActionPrintText(1, "texto", None)
    assert apt4._text == "texto" and apt4._printer == None
