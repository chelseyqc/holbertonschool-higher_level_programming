#!/usr/bin/python3
"""checks if obj is an instance of a_class"""


def inherits_from(obj, a_class):
    """
    checks if obj is an instance of a class

    Args:
        obj: the object
        a_class: the specified class

    Returns:
        True: if obj is an instance of a class inherited from a_class
        False: if not
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
