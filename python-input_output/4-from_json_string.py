#!/usr/bin/python3
"""
4-from_json_string module
"""


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): the JSON  string

    Returns:
        An object represented by a JSON string
    """
    import json
    return json.loads(my_str)
