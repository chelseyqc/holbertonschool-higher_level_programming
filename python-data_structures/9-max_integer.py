#!/usr/bin/python3
def max_integer(my_list=[]):
    # handle case when list is empty, loop doesn't start so max_num = None
    max_num = None
    for num in my_list:
        if max_num is None:
            max_num = num
        # check if challenger num is strong than champion max_num
        elif num > max_num:
            # if yes, challenger is the new champion
            max_num = num
    return max_num
