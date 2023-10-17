#!/usr/bin/python3
"""a class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class Square inherited from Rectangle"""
    def __init__(self, size):
        """instatiation with size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """area of the square"""
        area = self.__size ** 2
        return area

    def __str__(self):
        """square description"""
        return "[Square] {}/{}".format(self.__size, self.__size)
