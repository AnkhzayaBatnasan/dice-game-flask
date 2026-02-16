class DiceGame:
    def __init__(self):
        self.turn = 1
        self.point = None
        self.finished = False
        self.result = ""

    def is_valid_roll(self, roll):
        return 2 <= roll <= 12

    def play_turn(self, roll):
        if self.finished:
            return

        if not self.is_valid_roll(roll):
            self.result = "Error: Dice roll must be between 2 and 12."
            return

        if self.turn == 1:
            if roll in [2, 3, 12]:
                self.result = f"Turn {self.turn}: You rolled {roll}. You lose."
                self.finished = True
            elif roll in [7, 11]:
                self.result = f"Turn {self.turn}: You rolled {roll}. You win!"
                self.finished = True
            else:
                self.point = roll
                self.result = f"Turn {self.turn}: You rolled {roll}. Point is set to {self.point}."
                self.turn += 1
        else:
            if roll == 7:
                self.result = f"Turn {self.turn}: You rolled 7. You lose."
                self.finished = True
            elif roll == self.point:
                self.result = f"Turn {self.turn}: You rolled {roll}. You win!"
                self.finished = True
            else:
                self.result = f"Turn {self.turn}: You rolled {roll}. No result. Roll again."
                self.turn += 1
