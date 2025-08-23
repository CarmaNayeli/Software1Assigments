# prompt user for length and width and store as float variables
length = float(input("Enter the length of the rectangle: " ))
width = float(input("Enter the width of the rectangle: "))

# calculate perimeter and area and store as variables
perimeter = 2* (length + width)
area = length * width

# print results
print("The perimeter of the rectangle is " + str(perimeter))
print("The area of the rectangle is " + str(area))