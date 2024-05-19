#!/usr/bin/env python3
"""
Module for adding two matrices element-wise.
"""


def add_matrices2D(mat1, mat2):
    """
    Adds two matrices element-wise.

    Parameters:
    mat1 (list of lists): The first matrix.
    mat2 (list of lists): The second matrix.

    Returns:
    list of lists or None: A new matrix containing the result of adding corresponding
    elements of mat1 and mat2. Returns None if the matrices are not of the same shape.
    """
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)):
        return None
    return [
        [elem1 + elem2 for elem1, elem2 in zip(row1, row2)]
        for row1, row2 in zip(mat1, mat2)
    ]
