#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    copy = list(a_dictionary.items())
    for key, val in copy:
        if val == value:
            del a_dictionary[key]
    return a_dictionary
