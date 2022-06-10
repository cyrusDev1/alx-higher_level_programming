#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    ret = 0
    two = {'CM': 800, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
    one = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    while i < len(roman_string):
        if i < len(roman_string) - 1 and roman_string[i:i+2] in two:
            ret += two[roman_string[i:i+2]]
            i += 2
        else:
            ret += one[roman_string[i]]
            i += 1
    return ret
