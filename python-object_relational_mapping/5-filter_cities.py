#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database `hbtn_0e_4_usa`. The script is safe from
SQL injection.

Arguments:
    mysql username (str): The MySQL username.
    mysql password (str): The MySQL password.
    database name (str): The name of the database.
    state name (str): The name of the state to filter by.

Example usage:
    ./5-filter_cities.py root root hbtn_0e_4_usa Texas
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main code execution: Connects to the database, retrieves and displays
    cities of the given state.
    """
    # Get MySQL credentials and database details from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Use parameterized query to prevent SQL injection
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch and format the results
    cities = cursor.fetchall()
    city_names = [city[0] for city in cities]
    print(", ".join(city_names))

    # Close the cursor and database connection
    cursor.close()
    db.close()

