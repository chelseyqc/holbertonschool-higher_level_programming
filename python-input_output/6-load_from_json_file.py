#!/usr/bin/python3
"""
6-load_from_json_file module
"""


def load_from_json_file(filename):
    """
    creates an object from a JSON file

    Args:
        filename (str): the name of the file
    """
    import json
    with open(filename, 'r', encoding="utf8") as file:
        json.load(file)
