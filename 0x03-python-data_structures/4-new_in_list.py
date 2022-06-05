#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lens = len(my_list)
    if idx < 0 or idx >= lens:
        return my_list
    copy = my_list.copy()
    copy[idx] = element
    return copy
