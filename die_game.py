from random import randint

class Die:
    def __init__(self, sides = 6) :
        
        self.sides =sides

    def roll_die(self):
      appear = randint(1,6 )
      print(appear)
roll = Die(6)
for rl in range(1,10):

    roll .roll_die()

