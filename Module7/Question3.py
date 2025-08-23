# initialize dictionary for airports with key ICAO code: airport name
airports = {"code":"name"}
# initialize ICAO code, airport name, and option to none
ICAO = None
airport_name = None
option = None

# check if option is 3, if 3, exit
while option != 3:
    # print options menu
    print("")
    print("Airport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    # take option input
    option = int(input("Please choose an option (1-3): "))
    # if option one is chosen, enter a new airport into the dictionary
    if option == 1:
        # prompt for ICAO code
        ICAO = input("Enter the ICAO code: ")
        # prompt for airport name
        airport_name = input("Enter the airport name: ")
        # add entry to dictionary
        airports[ICAO] = airport_name
        # print confirmation
        print("Airport " + airport_name + " with ICAO code " + ICAO + " has been added.")

    # if option two is chosen, retrieve airport name with ICAO code
    elif option == 2:
        # prompt for ICAO code
        ICAO = input("Enter the ICAO code: ")
        # use given ICAO code to find airport name in dictionary and print
        try:
            print("The airport with ICAO code " + ICAO + " is " + airports[ICAO] + ".")
        # unless it's not in the dictionary, in which case throw an exception and return to the menu
        except:
            print("No airport found with ICAO code " + ICAO + ".")
    # if option three is chosen, thank you message and quit
    elif option == 3:
        print("Thank you for using the Airport Data Management system. Goodbye!")
        quit()
    # if anything else is entered, error message and return to menu
    else:
        print("Invalid input. Please try again.")
