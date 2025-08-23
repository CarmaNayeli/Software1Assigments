# import library to access random numbers
import random

# ask user for number of dice to roll
dice = input("How many dice to roll (use 1d20 format): ")
#split the input at the "d" symbol
try:
    dice = dice.split("d")
except:
    print("Invalid input")
    quit()
# put everything before the "d" in a variable - this is how many dice to roll
try:
    numDice = int(dice[0])
except:
    print("Invalid input")
    quit()
# put everything after the "d" in another variable - this is how many faces each die should have
try:
    faces = int(dice[1])
except:
    print("Invalid input")
    quit()
# initialize sum to 0
sumRolls = 0
#initialize current roll to None
current = None

#iterate from 0 to number given
for i in range(numDice):
    # roll a die
    current = random.randint(1,faces)
    #print the roll
    print(str(i + 1) + ": " + str(current))
    # add the roll to the sum
    sumRolls = sumRolls + current
# print sum
print("Sum of the dice: " + str(sumRolls))