class StateMachine:

    def __init__(self):
        self._current_state = None
        self._states = {}


    def register(self, state_name,state):
        self._states[state_name] = state
        state.machine = self


    def go_to(self, state_name, data=None):
        if self._current_state:
            self._current_state.exit()
        self._current_state = self._states[state_name]
        if self._current_state:
            self._current_state.enter(data)

    def up(self):
        self._current_state.up()


    def down(self):
        self._current_state.down()


    def left(self):
        self._current_state.left()


    def right(self):
        self._current_state.right()


    def select(self):
        self._current_state.select()


    def ok(self):
        self._current_state.ok()


    def shutter(self):
        self._current_state.shutter()
