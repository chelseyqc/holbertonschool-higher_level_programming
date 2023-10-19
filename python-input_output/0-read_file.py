#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (str): the name of the file to be read
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
