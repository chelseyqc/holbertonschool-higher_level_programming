#!/usr/bin/python3
"""a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """a class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor for the class"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """gets the width attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the width attribute"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """gets the height attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the height attribute"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """gets the x attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets the x attribute"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """gets the y attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets the y attribute"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of Rectangle"""
        return self.height * self.width

    def display(self):
        """prints the Rectangle instance in stdout with #"""
        if self.y > 0:
            print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """returns str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args,  **kwargs):
        """assigns an argument to each attribute"""
        if len(args) != 0:
            key = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, key[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the class"""
        keys = ["id", "width", "height", "x", "y"]
        rectangle_dict = {}
        for key in keys:
            rectangle_dict[key] = getattr(self, key)
        return rectangle_dict
