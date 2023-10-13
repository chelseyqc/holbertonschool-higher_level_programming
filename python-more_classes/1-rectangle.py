#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """
    defines a class Rectangle

    Args:
        width (int): private instance for the width of rectangle
        height (int): private instance for height of rectangle
    """
    
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        """initialise an instance of rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Gets the width attribute

        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width attribute

        Args:
            value (int): the width of the rectangle

        Raises:
            TypeError: if the width is not an int
            ValueError: if the width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the height attribute

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the height attribute

        Args:
            value (int): the height of the rectangle

        Raises:
            TypeError: if the height is not an int
            ValueError: if the height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
