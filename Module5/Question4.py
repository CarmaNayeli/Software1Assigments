# initialize blank list
cities = []
# initialize current city to none
current = None

# prompt for 5 cities and add them to the list
for i in range(0,5):
    current = input("Enter the name of a city: ")
    cities.append(current)

# print each city in the list in order of addition
print("The cities you entered:")
for i in cities:
    print(i)
