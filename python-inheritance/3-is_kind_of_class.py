#!/usr/bin/python3
"""checks if object is an instance of inherited class"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is instance of class or inherited class

    Args:
        obj: the object
        a_class: the class or inherited class

    Returns:
        True: if the object is an instance of the class
        False: if not
    """
    return isinstance(obj, a_class)
