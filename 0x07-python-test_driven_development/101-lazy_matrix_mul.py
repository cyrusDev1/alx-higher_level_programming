#!/usr/bin/python3
"""Matrix multiplication using NumPy.
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies m_a and m_b using
    matmul.
    """
    return np.matmul(m_a, m_b)
