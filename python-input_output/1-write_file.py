#!/usr/bin/python3
"""
1-write_file module
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file

    Args:
        filename (str): the file to be read
        text (str): the string

    Returns:
        int: the number of characters written
    """
    with open(filename, 'w', encoding="utf8") as file:
        return file.write(text)
