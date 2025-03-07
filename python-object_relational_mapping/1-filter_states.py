#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' (uppercase) 
from the database `hbtn_0e_0_usa`.

Arguments:
    mysql username (str): The MySQL username.
    mysql password (str): The MySQL password.
    database name (str): The name of the database.

Example usage:
    ./1-filter_states.py root root hbtn_0e_0_usa

Description:
    - Connects to a MySQL database using MySQLdb.
    - Retrieves and prints all states whose names start with 'N'.
    - The results are sorted in ascending order by `states.id`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main code execution: Connect to the database, retrieve and display the results.
    """

    # Get MySQL credentials and database name from command-line arguments
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

    # Execute the query to retrieve states with names starting with 'N'
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )

    # Fetch and print all rows
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

