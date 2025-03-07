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
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main code execution: Connect to the database, retrieve and display
    the results.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()

