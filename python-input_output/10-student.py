#!/usr/bin/python3
"""
Defines a Student class with JSON serialization capabilities.
"""


class Student:
    """
    Represents a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Return a dictionary representation of the Student instance.

        If attrs is a list of string, only those attribute will be retrieved.

        Args:
            attrs (list): list of attribute name to
            include in the dictionary(optional).

        Returns:
            dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return self.__dict__

        # Filter the dictionary to include only specified attributes
        filtered_dict = {
            key: value for key, value in self.__dict__.items() if key in attrs
        }
        return filtered_dict
        