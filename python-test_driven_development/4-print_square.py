#!/usr/bin/python3
"""prints a square"""


def print_square(size):
    """
    prints a square with the character #

    Args:
        size (int): the size length of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
