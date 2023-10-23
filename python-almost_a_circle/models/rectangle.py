#!/usr/bin/python3
"""a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """a class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for the class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """gets the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        self.__width = value

    @property
    def height(self):
        """gets the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        self.__height = value

    @property
    def x(self):
        """gets the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x attribute"""
        self.__x = value

    @property
    def y(self):
        """gets the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y attribute"""
        self.__y = value
