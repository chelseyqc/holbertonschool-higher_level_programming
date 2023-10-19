#!/usr/bin/python3
"""
5-save_to_json_file module
"""


def save_to_json_file(my_obj, filename):
    """
    Write an Object to a text file, using a JSON representation

    Args:
        my_obj: the object
        filename: the name of the text file
    """
    import json
    with open(filename, 'w', encoding="utf8") as file:
        json.dump(my_obj, file)
