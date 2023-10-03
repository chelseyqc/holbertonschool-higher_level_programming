#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    # initialised to None as there's no values yet
    highest = None
    highest_key = None
    for key in a_dictionary:
        # checks if the current value is higher than the current highest
        if highest is None or a_dictionary[key] > highest:
            # highest becomes current val, highest_key becomes current key
            highest = a_dictionary[key]
            highest_key = key
    # returns the key with the highest value in the dictionary
    return highest_key
