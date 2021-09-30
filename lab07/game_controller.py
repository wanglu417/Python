from die import Die
from pair_of_dice import PairOfDice


class GameController:
    """A controller for dice game"""
    def __init__(self):
        self.pair_of_dice = PairOfDice()
        self.VALUE1 = [7, 11]
        self.VALUE2 = [2, 3, 12]

    def start_play(self):
        """Start rolling two dies"""
        print(input("Press enter to roll the dice..."))
        self.pair_of_dice.roll_dice()
        self.lose_or_win()

    def lose_or_win(self):
        """Check the value for the first roll"""
        for i in self.VALUE1:
            if self.pair_of_dice.current_value() == i:
                print(
                    f"You rolled {self.pair_of_dice.current_value()}.You win!"
                )
                return
        for j in self.VALUE2:
            if self.pair_of_dice.current_value() == j:
                print(
                    f"You rolled {self.pair_of_dice.current_value()}.You lose."
                )
                return
        point = self.pair_of_dice.current_value()
        print("Your point is", self.pair_of_dice.current_value())
        self.keep_rolling(point)

    def keep_rolling(self, point):
        """Keep rolling if player does not win or lose in the first roll"""
        print(input("Press enter to roll the dice..."))
        self.pair_of_dice.roll_dice()
        if self.pair_of_dice.current_value() == point:
            print(f"You rolled {self.pair_of_dice.current_value()}. You win!")
        elif self.pair_of_dice.current_value() == 7:
            print(f"You rolled {self.pair_of_dice.current_value()}. You lose.")
        else:
            print(f"You rolled {self.pair_of_dice.current_value()}.")
            self.keep_rolling(point)
