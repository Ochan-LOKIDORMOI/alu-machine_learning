#!/usr/bin/env python3

def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenate two 2D matrices along a specified axis.

    This function takes two 2D matrices (represented as lists of lists) and
    concatenates them along the specified axis. If the axis is 0, the matrices
    are concatenated along the rows. If the axis is 1, the matrices are
    concatenated along the columns.

    Parameters:
    mat1 (list of lists): The first matrix to be concatenated.
    mat2 (list of lists): The second matrix to be concatenated.
    axis (int, optional): The axis along which to concatenate the matrices.
        If axis is 0, the matrices are concatenated along the rows.
        If axis is 1, the matrices are concatenated along the columns.
        Defaults to 0.

    Returns:
    list of lists: A new matrix resulting from the concatenation of mat1 and
        mat2 along the specified axis. Returns None if the concatenation is
        not possible (e.g., if the matrices have different dimensions along
        the non-concatenation axis).
    """
    if axis == 0:
        # Concatenate along the rows
        if len(mat1[0]) == len(mat2[0]):
            return mat1 + mat2
    elif axis == 1:
        # Concatenate along the columns
        if len(mat1) == len(mat2):
            return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    return None
