from abc import ABC, abstractmethod
import time

class CodeHandler(ABC):
    def __init__(self, next_handler):
        self._next_handler = next_handler

    @abstractmethod
    def handle_code(self, code, door):
        if self._next_handler is not None:
            self._next_handler.handle_code(code, door)
        else:
            pass

class Open(CodeHandler):
    def __init__(self, code, next_handler):
        self._code = code
        super().__init__(next_handler)
    def handle_code(self, code, door):
        if not door.locked:
            if code == self._code:
                door.reset_state()
                door.open()
            else:
                door._num_trials += 1
                #print("Incorrect code {} attempts left".format((3 - door._num_trials) if (3 - door._num_trials > 0) else 0))
                print("Incorrect code: trial {}".format(door._num_trials))
                super().handle_code(code, door)
        else:
            pass

class Lock(CodeHandler):
    def __init__(self, next_handler):
        super().__init__(next_handler)
    def handle_code(self, code, door):
        if door._num_trials >= 3:
            door.locked = True
            print("Door {} is now locked".format(door.id))
        super().handle_code(code, door)

class Unlock(CodeHandler):
    def __init__(self, code, next_handler):
        self._code = code
        super().__init__(next_handler)
    def handle_code(self, code, door):
        print("Handle opened")
        if door.locked:
            if code == self._code:
                door.reset_state()
                print("Door {} is now unlocked".format(door.id))
        else:
            super().handle_code(code, door)



class Log(CodeHandler):
    def __init__(self, next_handler):
        super().__init__(next_handler)

    def handle_code(self, code, door):
        if door.locked:
            state = "locked"
        else:
            state = "unlocked"
        print("Used code '{}' in door {}, current state : {} --- {}".format(code, door.id, state, time.asctime()))
        super().handle_code(code, door)


class FireAlarm(CodeHandler):
    def __init__(self, code, next_handler):
        self._code = code
        super().__init__(next_handler)

    def handle_code(self, code, door):
        if not door.locked:
            if code == self._code:
                door.open()
                print("Fire alarm triggered")
                door.reset_state()
            else:
                super().handle_code(code, door)
        else:
            super().handle_code(code, door)
