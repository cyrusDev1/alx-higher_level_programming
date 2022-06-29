#!/usr/bin/python3
"""Defines function that multiplies 2 matrices"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(line, list) for line in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(line, list) for line in m_b):
        raise TypeError("m_b must be a list of lists")

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    if (not all(isinstance(el, int) or isinstance(el, float)
                for line in m_a for el in line)):
        raise TypeError("m_a should contain only integers or floats")
    if (not all(isinstance(el, int) or isinstance(el, float)
                for line in m_b for el in line)):
        raise TypeError("m_b should contain only integers or floats")

    if not all(len(m_a[0]) == len(m_a[i]) for i in range(len(m_a))):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(m_b[0]) == len(m_b[i]) for i in range(len(m_b))):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    matrix = [[0 for i in range(len(m_b[0]))] for j in range(len(m_a))]

    matrix_line = len(matrix)
    matrix_colone = len(matrix[0])
    for i in range(matrix_line):
        for j in range(matrix_colone):
            element = 0
            for k in range(matrix_colone):
                element += m_a[i][k] * m_b[k][j]
            matrix[i][j] = element

    return matrix
