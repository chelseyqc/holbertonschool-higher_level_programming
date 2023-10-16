#!/usr/bin/python3
"""returns a list of available attributes and methods of an object"""


def lookup(obj):
    """
    Available attributes and methods

    Args:
        obj: an object

    Returns:
        list: a list of available attributes and methods
    """
    return dir(obj)
