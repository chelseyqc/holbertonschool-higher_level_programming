#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    else:
        new_string = ""
        for idx in my_string:
            new_string = my_string.translate({ord(idx): None for idx in 'Cc'})
        return new_string
