# I made this more complicated than necessary because I didn't like that it didn't handle not a number exceptions

# initiate variables for smallest and largest numbers and set reference variable
ref = 0
smallest = None
largest = None

# check that reference variable is not "", indicating quit
while ref != "":
    # set ref to user input
    ref = input("Enter a number (or press Enter to quit): ")
    # check if quit
    if ref != "":
        try:
            ref = float(ref)
        except:
            print("Invalid input, please try again using only numbers.")
            quit()
        # check if smallest has a value
        if smallest is not None:
            #check if input is less than the current smallest number
            if ref < smallest:
                # set smallest to input
                smallest = ref
        else:
            #set smallest to input
            smallest = ref
        # check if largest has a value
        if largest is not None:
            # check if input is greater than current largest number
            if ref > largest:
                #set largest to input
                largest = ref
        else:
            # set largest to input
            largest = ref
# check if smallest is initialized
if smallest is not None:
    # set smallest to float
    smallest = float(smallest)
    # print with one decimal place
    print(f"Smallest number: {smallest:.1f}")

#check is largest is initialized
if largest is not None:
    # set largest to float
    largest = float(largest)
    # print with one decimal place
    print(f"Largest number: {largest:.1f}")

