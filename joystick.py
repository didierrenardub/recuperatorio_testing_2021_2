
class Action():
    def __init__(self, id: int):
        self._id = id

    def id(self) -> int:
        return self._id

    def perform(self):
        raise NotImplementedError()


class Printer():
    def print(self, what: str):
        raise NotImplementedError()


class ActionPrintText(Action):
    def __init__(self, id: int, text: str, printer: Printer):
        Action.__init__(self, id)
        self._text = text
        self._printer = printer
        
    def perform(self):
        if self._printer is not None:
            self._printer.print(self._text)


class Button():
    def __init__(self, label: str, action: Action = None):
        self._label = label
        self._action = action

    def label(self) -> str:
        return self._label

    def press(self) -> bool:
        if self._action is not None:
            self._action.perform()
            return True
        return False


class Joystick():
    def __init__(self):
        self._buttons = []

    def add_button(self, button: Button) -> bool:
        if button not in self._buttons:
            self._buttons.append(button)
            return True
        return False

    def press(self, button_with_label: str) -> bool:
        for button in self._buttons:
            if button.label() == button_with_label:
                return button.press()
        return False
