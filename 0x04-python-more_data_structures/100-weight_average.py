#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    nume = 0
    deno = 0
    for i in range(len(my_list)):
        nume += (my_list[i][0] * my_list[i][1])
        deno += my_list[i][1]
    return nume / deno
