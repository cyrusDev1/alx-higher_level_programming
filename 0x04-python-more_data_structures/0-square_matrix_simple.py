#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    z = []
    for element in matrix:
        y = list(map(lambda x: x ** 2, element))
        z.append(y)
    return z
