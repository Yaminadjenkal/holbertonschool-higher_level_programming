#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database `hbtn_0e_6_usa`.

Arguments:
    mysql username (str): The MySQL username.
    mysql password (str): The MySQL password.
    database name (str): The name of the database.
    state name (str): The state name to search for.

Example usage:
    ./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Main code execution: Connects to the database and prints the State
    object with the provided name, or "Not found" if no state matches.
    """
    # Get MySQL credentials and database details from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Create the engine to connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query the State object with the provided name
    state = session.query(State).filter(State.name == state_name).first()

    # Display the result
    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    # Close the session
    session.close()

