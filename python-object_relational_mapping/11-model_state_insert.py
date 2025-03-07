#!/usr/bin/python3
"""
Script that adds the State object 'Louisiana' to the database `hbtn_0e_6_usa`
and prints its new `id`.

Arguments:
    mysql username (str): The MySQL username.
    mysql password (str): The MySQL password.
    database name (str): The name of the database.

Example usage:
    ./11-model_state_insert.py root root hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Main code execution: Connects to the database, adds a new State object,
    commits the transaction, and prints the new State's id.
    """
    # Get MySQL credentials and database details from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine to connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Create a new State object and add it to the session
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new State's id
    print(new_state.id)

    # Close the session
    session.close()

