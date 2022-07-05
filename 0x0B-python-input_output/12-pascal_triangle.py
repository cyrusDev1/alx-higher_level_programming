#!/usr/bin/python3
"""Defines pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists of integers representing
    the Pascal’s triangle of n"""
    triangle = []
    if n <= 0:
        return triangle

    for i in range(n):
        triangle.append([])

    for k in range(len(triangle)):
        i = 0
        while i <= k:
            if i == 0:
                triangle[k].append(1)
            elif i == k:
                triangle[k].append(1)
            else:
                triangle[k].append(triangle[k-1][i] + triangle[k-1][i-1])
            i += 1

    return triangle
