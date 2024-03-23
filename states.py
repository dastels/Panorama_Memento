#-------------------------------------------------------------------------------
# Abstract state defined do-nothing basic facilities

class State:

    def __init__(self, state_machine):
        self._state_machine = state_machine


    def enter(self, data):
        pass


    def exit(self):
        pass


    def up(self):
        pass


    def down(self):
        pass


    def left(self):
        pass


    def right(self):
        pass


    def select(self):
        pass


    def ok(self):
        pass


    def shutter(self):
        pass


#-------------------------------------------------------------------------------
# Default state from which you can enter the settings menu or take a panorama

class RunState(State):

    def __init(self):
        pass


    def enter(self):
        pass


    def exit(self):
        pass


    def left(self):
        self._state_machine.go_to('menu', 'pixel_ring')


    def right(self):
        self._state_machine.go_to('menu', 'pic_count')


    def shutter(self):
        pass


#-------------------------------------------------------------------------------
# Abstract value adjusting state

class ValueState(State):

    def __init__(self):
        self._value = 0


    def up(self):
        if self._value < self._max_value:
            self._value += 1
            # update display


    def down(self):
        if self._value > self._min_value:
            self._value -= 1
            # update display
