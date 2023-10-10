#!/usr/bin/python3
"""a class that defines a square"""


class Square:
    """
    Represents a square.

    Attributes:
    size (int): the size of the square
    area (int): the area of the square
    """
    def __init__(self, size=0):
        """
        initialises an instance of Square

        Args:
            size (int, optional): the size of a square. Defaults to 0
        """
        self.size = size

    @property
    def size(self):
        """
        Gets the size attribute

        Returns:
            int: the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size attribute

        Args:
            value (int): the size of the square

        Raises:
            TypeError: if the value is not an integer
            ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square

        Returns:
            int: the area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square in stdout with #

        Prints an empty line is the size is 0
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
