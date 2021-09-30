from die import Die


class PairOfDice:
    """Two dies"""
    def __init__(self):
        self.dice1 = Die()
        self.dice2 = Die()

    def roll_dice(self):
        self.dice1.roll()
        self.dice2.roll()

    def current_value(self):
        return int(self.dice1.current_value())
        +int(self.dice2.current_value())
