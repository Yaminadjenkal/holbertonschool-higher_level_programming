#!/usr/bin/python3
"""
Function to append string to textfile and return the number of character added.

"""


def append_write(filename="", text=""):
    """
    Append a string to UTF-8 textfile and return the number of character added.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The text to append to the file. Default to an empty string.

    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)