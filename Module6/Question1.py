# import library to access random number generator
import random

# function that generates a random number between 1 and 6 and returns that int
def roll_dice():
    return random.randint(1,6)

# roll first die
roll = roll_dice()
# if it's not a 6, print result and roll again
while roll != 6:
    print(roll)
    roll = roll_dice()
print(roll)
