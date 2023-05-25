import random

class game:
    def __init__(self):
        self.dices = random.randint(1,6)
        print(self.dices)
    
    def results(self):
        match self.dices:
            case 1:
                print("Move ONE square")
            case 2:
                print("Move TWO square")
            case 3:
                print("Move THREE square")
            case 4:
                print("Move FOUR square")           
            case 5:
                print("Move FIVE square")
            case 6:
                print("Move SIX square")

player_1 = game()
player_1.results()
