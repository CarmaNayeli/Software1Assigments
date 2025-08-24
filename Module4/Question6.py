# import library to access random numbers
import random

# set the total number of random points (N) to user input
N = int(input("Enter the number of random points to generate: "))
# initialize the number of random points that fall within the unit circle to 0
n = 0

# for each number from 0 until the total number of given points N, generate a random point
z = range(0, N)
for i in z:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # calculate and check if that point is inside the unit circle
    if ((x**2) + (y**2)) < 1:
        # if inside, increment n
        n += 1
# calculate approximation of pi
print("Approximation of pi:", 4*n/N)

#it took so long to format this correctly because the question does not specify and I hate this
