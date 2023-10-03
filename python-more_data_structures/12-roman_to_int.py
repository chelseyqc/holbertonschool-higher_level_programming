#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0
    r_dictionary = {
                    'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000
                    }
    # final int value
    total = 0
    # previous Roman numeral
    prev_val = 0
    for symbol in roman_string:
        # gets int val of current Roman numeral
        value = r_dictionary[symbol]
        # checks if current value > prev value
        if value > prev_val:
            # if yes, subtract twice the val of prev numeral from total
            total = total + value - 2 * prev_val
        else:
            total = total + value
        prev_val = value
    return total
