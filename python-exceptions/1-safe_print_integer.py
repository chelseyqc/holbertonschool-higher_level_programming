#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # prints value as an integer if no error and returns True
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # otherwise returns False
        return False
