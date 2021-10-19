from ..joystick import Action
from py import raises

def test_action_id():
    a = Action()
    assert a.id() == 0
    a1 = Action(0)
    assert a1.id() == 0
    a2 = Action(-5)
    assert a2.id() == -5
    a3 = Action(None)
    assert a3.id() == 0

def test_action_perform():
    a4 = Action(0)
    with raises(NotImplementedError):
        a4.perform() == 0

        