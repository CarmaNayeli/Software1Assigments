# define function to filter out odd numbers
def filter_even_numbers(list1):
    # initialize even-only list
    even = []
    # test if each number in list is even
    for number in list1:
        if number % 2 == 0:
            # if it is, add it to the even-only list
            even.append(number)
    # return even-only list
    return even

# initialize test list
testList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print original list
print("Original list:", testList)
# call function and print only the even numbers
print(f"List with even numbers only: {filter_even_numbers(testList)}")
