# import library for mysql connector python package
import mysql.connector

# define function to connect to database, query based on country code, and return a sorted dictionary
def get_airports_by_country(country_code):
    # Connect to the database - I used root@localhost for moodle, but you'd optimally use a real user with the correct privileges so to test it here I used the user I set up for my own local database
    conn = mysql.connector.connect(
        host="localhost",
        user="carma",
        password="Cde3xsw2",
        database="flight_game"
    )
    # open cursor in dictionary mode
    cursor = conn.cursor(dictionary=True)

    # execute the query
    cursor.execute("SELECT airport.name AS 'name', airport.type AS 'type' FROM airport, country WHERE airport.iso_country = country.iso_country AND country.iso_country = %s", (country_code,))
    result = cursor.fetchall()

    # initiate variables to count amount of each type
    num_closed = 0
    num_heli = 0
    num_large = 0
    num_med = 0
    num_small = 0
    num_sea = 0
    num_bal = 0

    # if any airports exist
    if result:
        # for every airport in the results
        for i in range(0,len(result)):
        # increment the correct variable for its type
            if (result[i]['type']) == "closed":
                num_closed += 1
            elif (result[i]['type']) == "heliport":
                num_heli += 1
            elif (result[i]['type']) == "large_airport":
                num_large += 1
            elif (result[i]['type']) == "medium_airport":
                num_med += 1
            elif (result[i]['type']) == "small_airport":
                num_small += 1
            elif (result[i]['type']) == "seaplane_base":
                num_sea += 1
            elif (result[i]['type']) == "balloonport":
                num_bal += 1
            # unless none exist, then close
            else:
                print("Error")

        # define initial dictionary using types and the number of each type
        airports_dict = {
            "closed": num_closed,
            "heliport": num_heli,
            "large_airport": num_large,
            "medium_airport": num_med,
            "small_airport": num_small,
            "seaplane_base": num_sea,
            "balloonport": num_bal
        }

        # this is the tricky part - use a lambda function to sort the dictionary by the number of keys reversed. If this wasn't already overkill I would spell out how I did it but uh. It is.
        sorted_dict = {k: v for k, v in sorted(airports_dict.items(), key=lambda item: item[1], reverse=True)}
        #return the sorted dictionary
        return sorted_dict

    # else give an error message and quit
    else:
        print(f"No airports found in with country code.")
        quit()
# define a function that calls the dictionary function and actually prints it
def run_country_program():
    # first prompt user for country code (making sure there is no white space and it's all uppercase)
    country_code = input("Enter the country code(eg, FI for Finland): ").strip().upper()
    # call first function to get the sorted dictionary
    airports = get_airports_by_country(country_code)
    # separate into keys and values for ease of printing
    airports_keys = list(airports.keys())
    airports_values = list(airports.values())

    # print formatted
    print("Airports in " + country_code + ":")
    for i in range(0, len(airports)):
        if airports_values[i] != 0:
            print(f"{airports_values[i]} {airports_keys[i]} airports")

#main, which calls second function
run_country_program()
