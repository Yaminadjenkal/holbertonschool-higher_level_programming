#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.

Arguments:
    mysql username (str): The MySQL username.
    mysql password (str): The MySQL password.
    database name (str): The name of the database.

Example usage:
    ./13-model_state_delete_a.py root root hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """
    Main code execution: Connects to the database, deletes State objects
    with a name containing the letter `a`, and commits the changes.
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

    # Query all State objects with a name containing the letter `a`
    states_to_delete = session.query(State).filter(State.name.like('%a%')).all()

    # Delete each matched State object
    for state in states_to_delete:
        session.delete(state)

    # Commit the changes to the database
    session.commit()

    # Close the session
    session.close()

