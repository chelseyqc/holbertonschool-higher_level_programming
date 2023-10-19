#!/usr/bin/python3
"""
2-append_write module
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file

    Args:
        filename (str): the name of the file
        text (str): the string

    Returns:
        int: the number of characters added
    """
    with open(filename, 'a', encoding="utf8") as file:
        # a mode appends to the end of the file
        return file.write(text)
