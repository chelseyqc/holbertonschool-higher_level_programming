#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """constructor for the class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints out the string"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """gets the size"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if len(args) != 0:
            key = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, key[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
