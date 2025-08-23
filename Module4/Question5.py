# initialize correct username and password (this would be a super insecure way to do this but the question doesn't specify)
correctUser = "python"
correctPass = "rules"
# initialize number of guesses to 1
guess = 1

#check that we haven't exceeded 5 guesses
while guess <= 5:
    #prompt for username and password
    guessUser = input("Enter username: ")
    guessPass = input("Enter password: ")

    # check if username and password are correct
    if guessUser == correctUser and guessPass == correctPass:
        # welcome message and end program
        print("Welcome")
        quit()
    else:
        #check if this is guess 5
        if guess == 5:
            #print access denied message
            print("Access denied")
        else:
            # prompt user to try again
             print("Incorrect username or password. Please try again.")
        # increment guesses
        guess += 1