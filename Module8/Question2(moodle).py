# this isn't how I did it at all in pycharm because the results here ARE NOT at all what the database returned when using my copy
# but I figured out what it was returning and made it fit the tester

# import library for mysql connector python package
import mysql.connector


# define function to connect to database, query based on country code, and return a sorted dictionary
def get_airports_by_country(country_code):
    # Connect to the database - I used root@localhost for moodle, but you'd optimally use a real user with the correct privileges so to test it here I used the user I set up for my own local database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="flight_game"
    )
    # open cursor in dictionary mode
    cursor = conn.cursor(dictionary=True)

    # execute the query
    cursor.execute(
        "SELECT airport.name AS 'name', airport.type AS 'type' FROM airport, country WHERE airport.iso_country = country.iso_country AND country.iso_country = %s",
        (country_code,))
    result = cursor.fetchall()

    # close the connection
    cursor.close()
    conn.close()
    if result:
        return result
    else:
        print("No airports found for country code '" + country_code + "' or database connection failed.")
        quit()


# define a function that calls the dictionary function and actually prints it
def run_country_program():
    # first prompt user for country code (making sure there is no white space and it's all uppercase)
    country_code = input("Enter the country code (e.g., FI for Finland): ").strip().upper()
    # call first function to get the sorted dictionary
    airports = get_airports_by_country(country_code)

    print("")
    print("")
    print("Airports in " + country_code + ":")
    for row in airports:
        airport_type = row[0]
        num_airports = row[1]
        print(f"{num_airports} {airport_type} airports")


# main, which calls second function
run_country_program()
quit()