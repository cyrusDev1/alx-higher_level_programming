#!/usr/bin/python3
"""Defines matrix divided function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.

    Args:
        matrix (list): A list of lists of ints or floats.
        div (int/float): The divisor.
    Raises:
        TypeError: If the matrix contains non-numbers.
        TypeError: If the matrix contains rows of different sizes.
        TypeError: If div is not an int or float.
        ZeroDivisionError: If div is 0.
    Returns:
        A new matrix representing the result of the division.
    """
    new_matrix = []
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(lt, list) for lt in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if (not all(isinstance(elmt, int) or isinstance(elmt, float)
                for elmt in [elm for i in matrix for elm in i])):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if not all(len(matrix[0]) == len(lt) for lt in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for lt in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), lt)))

    return new_matrix
