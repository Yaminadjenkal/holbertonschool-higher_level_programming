#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the `states`
table of `hbtn_0e_0_usa` where `name` matches the argument.

Arguments:
    mysql username (str): The MySQL username.
    mysql password (str): The MySQL password.
    database name (str): The name of the database.
    state name (str): The state name to search for.

Example usage:
    ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main code execution: Connects to the database, retrieves and displays
    states matching the user input.
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

    # Format the query using the user input
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(state_name)

    # Execute the SQL query
    cursor.execute(query)

    # Fetch and display the results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

