#!/usr/bin/env python3

# cat_matrices2D = __import__('7-gettin_cozy').cat_matrices2D

def cat_matrices2D(mat1, mat2, axis=0):
    if axis == 0:
        # Concatenate along the rows
        if all(len(row) == len(mat1[0]) for row in mat2):
            return mat1 + mat2
    elif axis == 1:
        # Concatenate along the columns
        if len(mat1) == len(mat2):
            return [row1 + row2 for row1, row2 in zip(mat1, mat2)]
    return None
