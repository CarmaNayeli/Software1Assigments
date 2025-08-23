# import library to access random numbers
import random

# ask user for number of dice to roll
numDice = int(input("How many dice to roll: "))
# initialize sum to 0
sumRolls = 0

#iterate from 0 to number given
for i in range(numDice):
    #add number rolled 1-6 to sum
    sumRolls = sumRolls + random.randint(1,6)
# print result
print("Sum of the dice: " + str(sumRolls))
