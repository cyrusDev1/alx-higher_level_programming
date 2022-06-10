#!/usr/bin/python3
def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) and len(a_dictionary) > 0:
        all_key = list(a_dictionary.keys())
        key = all_key[0]
        for k , v in a_dictionary.items():
            if v > a_dictionary[key]:
                key = k
        return key
    else:
        return None
