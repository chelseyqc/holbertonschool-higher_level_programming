#!/usr/bin/python3
"""
3-to_json_string module
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string)

    Args:
        my_obj (str): the object

    Returns:
        JSON representation of an object
    """
    import json
    return json.dumps(my_obj)
