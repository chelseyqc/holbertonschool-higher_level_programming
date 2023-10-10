#!/usr/bin/python3
"""a class that defines a square"""


class Square:
    """
    Represents a square.

    Attributes:
    size (int): the size of the square
    position (int): the position of the square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialises an instance of Square

        Args:
            size (int, optional): the size of a square. Defaults to 0
            position (tuple, optional): the position of the square.
        """
        self.size = size
        self.position = position

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
        Sets the size attributes

        Args:
            value (int): the size of the square
        Raises:
            TypeError: if the value if not an integer
            ValueError: if the value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Gets the position attribute

        Returns:
            tuple: the position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position attribute

        Args:
            value (tuple): The position of the square

        Raises:
            TypeError: if the value is not a tuple of 2 positive integers
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
            not all(isinstance(num, int) and num >= 0 for num in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

        Prints an empty line if the size is 0
        """
        if self.__size == 0:
            print("")
        else:
            print("\n" * self.position[1], end="")
            for _ in range(self.__size):
                print(" " * self.position[0] + "#" * self.__size)
