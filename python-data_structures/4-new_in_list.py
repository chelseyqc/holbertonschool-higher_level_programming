#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        new_list = my_list.copy()
        new_list.remove(idx + 1)
        new_list.insert(idx, element)
        return new_list
