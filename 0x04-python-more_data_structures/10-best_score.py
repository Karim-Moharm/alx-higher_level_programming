#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    
    first_key = list(a_dictionary.keys())[0]
    first_value = a_dictionary[first_key]
    max_key = str()

    for key, value in a_dictionary.items():
        if value > first_value:
            first_value = value
            max_key = key
    return max_key
