#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for i in range(len(my_list)):
        if search == my_list[i]:
            new.append(replace)
        else:
            new.append(my_list[i])
    return (new)
