# ask user for length of fish
length = float(input("Enter the length of the zander in centimeters: "))

# calculate missing centimeters
missing_centimeters = 42 - length

# print message to return fish if below 42cm
if missing_centimeters > 0:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {missing_centimeters:2.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")