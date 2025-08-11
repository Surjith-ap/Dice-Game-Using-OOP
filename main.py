import random


class Die:

    def __init__(self):
        self._value = None

    @property
    def value(self):
        return self._value
    

    def roll(self):
        new_value = random.randint(1, 6)
        self._value = new_value
        return new_value




        