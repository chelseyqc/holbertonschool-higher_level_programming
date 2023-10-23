#!/usr/bin/python3
"""a class Base"""


class Base:
    """
    a class Base
    """
    __nb__objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb__objects = Base.__nb__objects + 1
        self.__nb__objects = id
