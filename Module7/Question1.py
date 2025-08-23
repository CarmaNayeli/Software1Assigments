# define function to determine season from month number
def get_season(month):
    # if the month number is 12, 1, or 2, return string winter
    if (month == 12) or (month == 1) or (month == 2):
        return "winter"
    # if the month number is 3, 4, or 5, return string spring
    elif (month == 3) or (month == 4) or (month == 5):
        return "spring"
    # if the month number is 6, 7, or 8, return string summer
    elif (month == 6) or (month == 7) or (month == 8):
        return "summer"
    # if the month number is 9, 10, or 11, return string autumn
    elif (month == 9) or (month == 10) or (month == 11):
        return "autumn"
    # if any other value was entered, error message and quit program
    else:
        print("Please enter a number between 1 and 12.")
        quit()

# prompt user to enter month number
monthnum = int(input("Enter the number of a month (1-12): "))
# print the chosen number
print("You entered: " + str(monthnum))
# call function to determine season
season = get_season(monthnum)
# print the season
print("The season is " + season + ".")
