# import library to access random number generator
import random

# function that generates a random number between 1 and the parameter given and returns that int
def roll_dice(face):
    return random.randint(1,face)

# prompt user for number of faces
face = int(input("Number of faces: "))
# roll first die
roll = roll_dice(face)
# if it's not the maximum, print result and roll again
while roll != face:
    print(roll)
    roll = roll_dice(face)
print(roll)