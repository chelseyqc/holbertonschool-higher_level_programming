#!/usr/bin/python3
"""Checks if obj is exactly an instance of specified class"""


def is_same_class(obj, a_class):
    """check if obj is in a_class"""
    return type(obj) == a_class
