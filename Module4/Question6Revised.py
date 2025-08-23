# I realized I probably wasn't supposed to use a for loop yet, so I rewrote it with a while loop

# import library to access random numbers
import random

# set the total number of random points (N) to user input
N = int(input("Enter the number of random points to generate: "))
# set the number of random points that fall within the unit circle to 0
n = 0
# initialize a reference variable
points = 0

# for each number from 0 until the total number of given points N, generate a random point
while points <= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # calculate and check if that point is inside the unit circle
    if ((x**2) + (y**2)) < 1:
        # if inside, increment n
        n += 1
    # increment reference
    points += 1

# calculate approximation of pi
approxPI = (4*n)/N

#print answer
print(f"Approximation of pi based on {N:.0f} points: ")
print(approxPI)
