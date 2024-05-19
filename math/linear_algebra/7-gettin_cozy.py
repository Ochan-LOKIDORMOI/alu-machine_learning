#!/usr/bin/env python3

def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Parameters:
    mat1 (list of lists): The first matrix.
    mat2 (list of lists): The second matrix.
    The axis along which to concatenate the matrices.
        If axis is 0, concatenates along the rows.
        If axis is 1, concatenates along the columns.

    Returns:
    A new matrix resulting from concatenating mat1 and mat2
    along the specified axis.
    """
    if axis == 0:
        # Concatenate along the rows
        if all(len(row) == len(mat1[0]) for row in mat2):
            return mat1 + mat2
    elif axis == 1:
        # Concatenate along the columns
        if len(mat1) == len(mat2):
            return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    return None
