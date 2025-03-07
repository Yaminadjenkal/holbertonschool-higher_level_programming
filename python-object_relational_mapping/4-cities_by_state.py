#!/usr/bin/python3
"""
Script that lists all cities from the database `hbtn_0e_4_usa`.

Arguments:
    mysql username (str): The MySQL username.
    mysql password (str): The MySQL password.
    database name (str): The name of the database.

Example usage:
    ./4-cities_by_state.py root root hbtn_0e_4_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main code execution: Connects to the database, retrieves and displays
    all cities sorted by `cities.id`.
    """
    # Get MySQL credentials and database details from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute the SQL query to retrieve all cities with their corresponding states
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch and display all rows
    cities = cursor.fetchall()
    for city in cities:
        print(city)

    # Close the cursor and database connection
    cursor.close()
    db.close()

