#!/usr/bin/python3
"""Function to read a text file and print its contents to stdout."""


def read_file(filename=""):
    """Reads a UTF-8 text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read. Default to empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")