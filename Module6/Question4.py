#define a function to sum a list of integers
def sum_of_list(list1):
    #find length of list
    length = len(list1)
    # initialize sum to 0
    sum1 = 0
    # add integers from 0 to length to sum
    for i in range(0,length):
        sum1 = sum1 + list1[i]
    # return sum
    return sum1

# initialize a test list
a_list = [1,2,3,4,5]

# call function and print the sum
print(f"The sum of the numbers in the list is: {sum_of_list(a_list)}")