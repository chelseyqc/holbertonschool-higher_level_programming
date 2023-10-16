#!/usr/bin/python3
"""a class MyList"""

class MyList(list):
    """a class MyList that inherits from list"""
    def print_sorted(self):
        """prints the list sorted in ascending order"""
        sort_list = sorted(self)
        print(sort_list)
