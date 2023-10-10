#!/usr/bin/python3
"""
A Function that adds 2 integers
"""


def add_integer(a, b=98):
    """
    sum of 2 integers

    Args:
        a (int): an integer thats added with b
        b (int): the other integer thats added with a

    Returns: 
        int: the result of the sum of a and b 
    """
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    elif b is None or (type(b) is not int and type(b) is not float):
        raise TypeError("b must be an integer")
    result = int(a) + int(b)
    return result
