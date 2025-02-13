#!/usr/bin/python3
"""
Function write a string to textfile and return the number of character written.

"""


def write_file(filename="", text=""):
    """
    Write string to UTF-8 textfile and return the number of character written.

    Args:
        filename (str): The name of the file to write to.
        Defaults to an empty string.
        text (str): The text to write to the file. Defaults to an empty string.

    Returns:
        int: The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
    