#!/usr/bin/python3
"""
Script to create the `states` table in the database using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database details from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create the engine and connect to the database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(username, password, database),
        pool_pre_ping=True
    )

    # Create all tables defined by Base (in this case, only `states`)
    Base.metadata.create_all(engine)

