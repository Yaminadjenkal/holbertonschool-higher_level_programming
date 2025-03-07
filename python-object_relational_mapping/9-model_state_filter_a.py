#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter `a`
from the database `hbtn_0e_6_usa`.

Arguments:
    mysql username (str): The MySQL username.
    mysql password (str): The MySQL password.
    database name (str): The name of the database.

Example usage:
    ./9-model_state_filter_a.py root root hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Main code execution: Connects to the database and lists all State objects
    containing the letter 'a', sorted by id.
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

    # Query State objects containing 'a', sorted by id
    states = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    # Display each state's id and name
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

