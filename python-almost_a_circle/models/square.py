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
