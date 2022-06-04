#!/usr/bin/python3
def element_at(my_list, idx):
    lens = len(my_list)
    if idx < 0 or idx >= lens:
        return None
    elm = my_list[idx]
    return elm
