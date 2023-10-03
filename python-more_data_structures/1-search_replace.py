#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # compact for loop that iterates over my_list
    # checks if old_item is equal to search, if yes, it puts in replace
    # else it puts in old_item in the new_list
    new_list = [replace if old_item == search else old_item for old_item in my_list]
    return new_list
