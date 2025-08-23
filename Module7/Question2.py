# define function to see if a name has already appeared in the list
def duplicate_finder(name, list):
    # for each entry in the list, see if the name is the same
    for i in list:
        # if the name is identical to one already in the list, return True
        if i == name:
            return True
    # if the name does not previously appear in the list, return False
    return False

# initialize list of names as a set
names =  set()
# ask user for first name
name= input("Enter a name: ")
# exit if blank string immediately entered
if name == "":
    quit()
# check for duplicates, add to list if new, ask for another name
while name != "":
    if duplicate_finder(name, names):
        print("Existing name")
        name = input("Enter a name: ")
    else:
        print("New name")
        names.add(name)
        name = input("Enter a name: ")
# print the whole list
print(names)
