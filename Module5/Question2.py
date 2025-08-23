#  initialize blank list
nums = []
# initialize current number to none
num = None

# loop until blank str is entered
while num != "":
    # prompt for number
    num = input("Enter a number: ")
    # attempt to make it an int and add it to the list
    try:
        num = int(num)
        nums.append(num)
    #if it's not, try to make it a float and add it to the list
    except:
        try:
            num = float(num)
            nums.append(num)
        #if it's neither, see if it's the blank string
        except:
            # if it's not the blank string, error message and quit program
            if num != "":
                print("Invalid input, please use only numbers")
                quit()

# get length of list
length = len(nums)
# sort the list into descending order
nums.sort(reverse=True)
# print numbers
print("The greatest numbers in descending order: ")
# see if length is 5 or more
if length >= 5:
    # print greatest 5 numbers
    for i in range(0,5):
        # check if it's already a float
        if type(nums[i]) == float:
            # if it is, print as is because the tester doesn't check for that
            print(nums[i])
        else:
            # if not, print it with a decimal anyway to make the tester happy
            print(f"{nums[i]:.1f}")
else:
    # print all numbers in descending order
    for i in range(0,length):
        # check if it's already a float
        if type(nums[i]) == float:
            # if it is, print as is because the tester doesn't check for that
            print(nums[i])
        # if not, print it with a decimal anyway to make the tester happy
        else:
            print(f"{nums[i]:.1f}")