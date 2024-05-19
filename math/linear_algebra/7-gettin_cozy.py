#!/usr/bin/env python3

def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Parameters:
    mat1 (list of lists): The first matrix.
    mat2 (list of lists): The second matrix.
    axis (int, optional): The axis along which to concatenate the matrices.
        If axis is 0, concatenates along the rows.
        If axis is 1, concatenates along the columns. Defaults to 0.

    Returns:
    list of lists or None: A new matrix resulting from concatenating mat1 and mat2
    along the specified axis. Returns None if concatenation is not possible.
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
