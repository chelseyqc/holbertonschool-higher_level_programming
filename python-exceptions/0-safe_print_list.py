#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    for i, element in enumerate(my_list):
        try:
            if i < x:
                print(element, end="")
                length = length + 1
            else:
                break
        except IndexError:
            break
    print()
    return length
