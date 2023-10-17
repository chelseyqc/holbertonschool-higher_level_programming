#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """
    a class BaseGeometry
    """
    def area(self):
        """not yet implemented"""
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        validates value
        
        Args:
            name (str): the name inputted
            value (int): the value inputted
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
