# import library for mysql connector python package
import mysql.connector


# define function to get the info of the airport based on ICAO
def get_info(icao_code):
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
    cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao_code,))
    result = cursor.fetchone()

    # output result if result exists
    if result:
        print(f"Airport name: {result['name']} \nLocation: {result['municipality']}")
    # else give an error message
    else:
        print(f"No airport found with ICAO code " + icao_code)

    # close the connection
    cursor.close()
    conn.close()


# Ask user for ICAO code (strip whitespace and convert to uppercase)
icao_code = input("Enter the ICAO code of an airport: ").strip().upper()
# call function using that ICAO
get_info(icao_code)
# quit the program manually because if I don't add this the shell adds a linebreak and the moodle tester doesn't like that
quit()
