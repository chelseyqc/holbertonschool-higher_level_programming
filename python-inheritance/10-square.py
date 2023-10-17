#!/usr/bin/python3
"""class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""
    def __init__(self, size):
        """instatiation of size"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        area = self.__size ** 2
        return area
