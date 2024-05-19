#!/usr/bin/env python3
"""
Matrix multiplication
"""


def mat_mul(mat1, mat2):
    """
    Returns
    m_array: multiplied matrices
    """
    m_array = [
        [0 for _ in range(len(mat2[0]))]
        for _ in range(len(mat1))
    ]

    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                m_array[i][j] += mat1[i][k] * mat2[k][j]

    return m_array
