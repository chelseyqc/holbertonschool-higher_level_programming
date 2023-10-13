#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """
    defines a class Rectangle

    Attributes:
        width (int): the width of the rectangle
        height (int): the height of the rectangle
        area (int): the area of the rectangle
        perimeter (int): the perimeter of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Gets the attribute width

        Returns:
            int: the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the attribute width

        Args:
            value (int): the width of the rectangle

        Raises:
            TypeError: if the width is not an int
            ValueError: if the width is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Gets the attribute height

        Returns:
            int: the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the attribute height

        Args:
            value (int): the height of the rectangle

        Raises:
            TypeError: if height is not an int
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

        Returns: the area of the rectangle
        """
        area = self.width * self.height
        return area

    def perimeter(self):
        """
        The rectangle's perimeter

        Returns: the perimeter of the rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        perimeter = (self.width * 2) + (self.height * 2)
        return perimeter

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)
