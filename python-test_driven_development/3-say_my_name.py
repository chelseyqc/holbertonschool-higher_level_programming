#!/usr/bin/python3
"""prints a string for first and last name"""


def say_my_name(first_name, last_name=""):
    """
    prints "My name is <first name> <last name>"

    Args:
        first_name (str): the first name inputted
        last_name (str): the last name inputted

    Prints the first name and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
