# import math library for access to pi
import math

# define function to calculate unit price based on diameter(cm) and price (euros)
def calculate_unit_price(diameter,price):
    # calculate radius in meters
    radius_m = (diameter / 2) * 0.01
    # calculate area of pizza in meters
    area = math.pi * radius_m * radius_m
    # divide price by area to get unit price
    unit_price = price / area
    # return unit price
    return unit_price

# Ask user for diameter and price of first pizza
diameter1 = int(input("Enter the diameter of the first pizza (cm): "))
price1 = int(input("Enter the price of the first pizza (euros): "))
# call function to calculate unit price
unit_price1 = calculate_unit_price(diameter1,price1)
# Ask user for diameter and price of second pizza
diameter2 = int(input("Enter the diameter of the second pizza (cm): "))
price2 = int(input("Enter the price of the second pizza (euros): "))
# call function to calculate unit price
unit_price2 = calculate_unit_price(diameter2,price2)

# print both unit prices
print(f"Unit price of the first pizza: {unit_price1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unit_price2:.2f} euros/m²")

# compare unit prices and print result
if unit_price1 < unit_price2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")