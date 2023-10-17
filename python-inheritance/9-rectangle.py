#!/usr/bin/python3
"""a class Rectangle"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a Rectangle that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """instatiation with width and height"""
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)
        self.__width = width
        self.__height = height

    def area(self):
        area = self.__width * self.__height
        return area

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
