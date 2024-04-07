
class Door:
    def __init__(self, id, code_handler):
        self.id = id
        self._code_handler = code_handler
        self._num_trials = 0
        self.locked = False

    def process_code(self, code):
        self._code_handler.handle_code(code, self)

    def open(self):
        print("open door {}".format(self.id))

    def reset_state(self):
        self._num_trials = 0
        self.locked = False
