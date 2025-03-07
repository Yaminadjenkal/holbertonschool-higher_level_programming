#!/usr/bin/python3
"""
Module defining the State class and creating an instance of declarative_base().
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create the declarative base instance
Base = declarative_base()


class State(Base):
    """
    Class that defines the `states` table in the database.
    Inherits from SQLAlchemy Base.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

