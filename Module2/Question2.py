#import math library
from math import pi
# prompt user for radius and store as float variable
radius = float(input("Enter the radius of the circle: "))

# calculate area and store as variable
area = radius * radius * pi

# print area
print("The area of the circle is " + str(area))
