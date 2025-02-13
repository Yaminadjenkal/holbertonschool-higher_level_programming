#!/usr/bin/python3
"""
Define a Student class with serialization and deserialization capabilitie.
"""


class Student:
    """Represents a student with first name, last name, and age."""

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
        Returns a dictionary representation of the Student instance.

        If attrs is a list of string, only those attribute will be retrieved.

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

    def reload_from_json(self, json):
        """Replace all attribute of Student instance wit those from dictionary.
        """
        for key, value in json.items():
            setattr(self, key, value)
                