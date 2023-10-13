#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """
    defines a class Rectangle

    Args:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        area (int): the area of the rectangle
        perimeter (int): the perimeter of a rectangle
    """

    def __init__(self, width=0, height=0):
        """initialise an instance of rectangle"""
        self.width = width
        self.height = height

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
            TypeError: if width is not an int
            ValueError: if width is less than 0
        """
        if type(value) is not int:
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        The rectangle's area

        Returns:
            int: the area of the rectangle
        """
        area = self.height * self.width
        return area

    def perimeter(self):
        """
        The rectangle's perimeter

        Returns:
            int: the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        perimeter = (self.height * 2) + (self.width * 2)
        return perimeter
