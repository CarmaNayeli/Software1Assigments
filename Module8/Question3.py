# import library for mysql connector python package
import mysql.connector
#import library for geopy so we can calculate distance between coordinates
from geopy.distance import geodesic

# define function to grab the coordinates from the database based on icao
def get_airport_coordinates(icao):
    # Connect to the database - I used root@localhost for moodle, but you'd optimally use a real user with the correct privileges so to test it here I used the user I set up for my own local database
    conn = mysql.connector.connect(
        host="localhost",
        user="carma",
        password="Cde3xsw2",
        database="flight_game"
    )

    # open cursor
    cursor = conn.cursor()
    # execute database query
    cursor.execute("SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s;", (icao,))
    # get results
    result = cursor.fetchone()
    # turn results into a coordinate pair
    try:
        coords = (result[0],result[1])
    except:
        print("Airport with ICAO code " + icao + " not found in the database.")
        quit()
    # close the connection
    cursor.close()
    conn.close()
    # return coordinate pair
    return coords

# define function to calculate the distance based on the coordinates
def run_airport_distance():
    # ask user for first ICAO code
    icao1 = input("Enter the ICAO code of the first airport: ")
    # ask user for second ICAO code
    icao2 = input("Enter the ICAO code of the second airport: ")
    #call first function to get coords for each
    coords1 = get_airport_coordinates(icao1)
    coords2 = get_airport_coordinates(icao2)
    # calculate distance with geopy
    dist_km = geodesic(coords1, coords2).kilometers
    #print formatted result
    print(f"\n\nDistance between {icao1} and {icao2}: {dist_km:.2f} kilometers")

# main which calls distance function
run_airport_distance()
quit()