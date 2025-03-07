#!/usr/bin/python3
"""
Script to list all states from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor to execute SQL queries
    cursor = db.cursor()

    # Execute the query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and print all rows
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

