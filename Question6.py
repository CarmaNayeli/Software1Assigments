#import library to access random numbers
import random

# print 3-digit code
print("3-digit code: " + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))

# print 4-digit code
print("4-digit code: " + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)))