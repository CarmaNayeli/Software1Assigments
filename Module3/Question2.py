# ask user for cabin class
cabin = input("Enter the cabin class (LUX, A, B, or C): ")

# print message based on cabin class
if cabin == "LUX":
    print("Upper-deck cabin with a balcony.")
elif cabin == "A":
    print("Above the car deck, equipped with a window.")
elif cabin == "B":
    print("Windowless cabin above the car deck.")
elif cabin == "C":
    print("Windowless cabin below the car deck.")
# error message for invalid input
else:
    print("Invalid cabin class.")