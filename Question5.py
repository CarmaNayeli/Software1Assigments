# prompt user for integers and store
talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

# calculate sum, product, and average, and store as variables
total_grams = (talents * 8512) + (pounds * 425.6) + (lots * 13.3)
kilograms = int(total_grams / 1000)
remaining_grams = total_grams % 1000

# print results
print("The weight in modern units:")
print(str(kilograms) + f" kilograms and {remaining_grams:4.2f} grams.")