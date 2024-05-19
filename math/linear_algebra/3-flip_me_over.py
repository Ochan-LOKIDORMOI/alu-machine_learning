#!/usr/bin/env python3
"""
Module for transposing a matrix.
"""


def matrix_transpose(matrix):
    """
    Transposes a matrix.

    Parameters:
    matrix (list of lists): The matrix to be transposed.

    Returns:
    list of lists: The transposed matrix, where rows become columns and vice versa.
    """
    return [
        list(row) for row in zip(*matrix)
    ]
