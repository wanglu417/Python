import random


class Die:
    """A single die"""

    def __init__(self):
        self.current_value1 = []

    def roll(self):
        values = ["1", "2", "3", "4", "5", "6"]
        self.current_value1.append(random.choice(values))

    def current_value(self):
        return int(self.current_value1[-1])
