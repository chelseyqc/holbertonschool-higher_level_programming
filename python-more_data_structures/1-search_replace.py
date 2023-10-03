#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # compact for loop that iterates over my_list
    # checks if old is equal to search, if yes, it puts in replace
    # else it puts in old in the new_list
    new_list = [replace if old == search else old for old in my_list]
    return new_list
