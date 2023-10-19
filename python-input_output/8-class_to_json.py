#!/usr/bin/python3
"""
8-class_to_json module
"""


def class_to_json(obj):
    """
    Dictionary description with simple data structure

    Args:
        obj: an instance of a Class

    Returns:
        A dictionary of all the obj's attributes
    """
    return obj.__dict__
