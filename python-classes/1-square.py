#!/usr/bin/python3
"""a class Square that defines a square"""


class Square:
    """
    Represents a square.

    Attributes:
    __size (int): the size of the square

    Methods:
    __init__(self, size): Initialises an instance of the Square class
    """
    def __init__(self, size):
        """
        initialise an instance of Square

        Args:
        size (int): the size of the square
        """
        self.__size = size
