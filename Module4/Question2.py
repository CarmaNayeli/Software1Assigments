# ask user for length in inches
inches = 0

# print calculation of length in centimeters until input is negative
while inches >= 0:
    inches = float(input("Enter length in inches (negative value to quit): "))
    if inches >= 0:
        print(f"{inches:.1f} inches is {(inches * 2.54):.2f} centimeters")
    else:
        print("Program ended.")