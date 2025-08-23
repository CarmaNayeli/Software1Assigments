# import math library
import math

# ask user for an integer
try:
    # test that it's actually an integer
    num = int(input("Enter an integer: "))
except:
    # if not, error and quit
    print("Invalid input")
    quit()

# test if the integer is 1 or less, in which case it's not a prime number (1, 0, and negative numbers are by definition not prime)
if num <=1:
    print(f"{num} is not a prime number.")
# if it's a positive integer, test if it's divisible by each number from 2 to the number's square root +1 (which is the highest number it could possibly be divided by besides itself)
else:
    for i in range(2, int(math.sqrt(num))+1):
        # if it ever divides without a remainder, it is not prime
        if num % i == 0:
            print(f"{num} is not a prime number.")
            quit()
    # if it gets here, it is prime
    print(f"{num} is a prime number.")