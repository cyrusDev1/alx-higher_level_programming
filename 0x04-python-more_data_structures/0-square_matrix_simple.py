#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    z = []
    for l in matrix:
        y = list(map(lambda x: x ** 2, l))
        z.append(y)
    return z
