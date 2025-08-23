# import library to access random numbers
import random

# set computer's number to a random integer between 1 and 10
comp = random.randint(1, 10)
# initialize guessed number
guess = None

# check that the guessed number is not the same as the computer's number
while guess != comp:
    # prompt for guess
    guess = int(input("Guess a number (1-10): "))
    # check if guess is lower
    if guess < comp:
        print("Too low")
    # check if guess is higher
    elif guess > comp:
        print("Too high")

# if it gets here, guess must be the same as comp, so print correct
print("Correct")