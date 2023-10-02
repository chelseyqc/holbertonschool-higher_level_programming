#!/usr/bin/python3
def no_c(my_string):
    for idx in my_string:
        new_string = my_string.translate({ord(idx): None for idx in 'Cc'})
        return new_string
