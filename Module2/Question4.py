# prompt user for integers and store
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# calculate sum, product, and average, and store as variables
sum_of_numbers = num1 + num2 + num3
product_of_numbers = num1 * num2 * num3
average_of_numbers = float(sum_of_numbers / 3)

# print results
print("The sum of the numbers: " + str(sum_of_numbers))
print("The product of the numbers: " + str(product_of_numbers))
print("The average of the numbers: " + str(average_of_numbers))