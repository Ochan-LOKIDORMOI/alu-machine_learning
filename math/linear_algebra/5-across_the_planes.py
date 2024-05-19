#!/usr/bin/env python3

def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2) or any(len(row1) != len(row2) for row1, row2 in zip(mat1, mat2)):
        return None
    return [[elem1 + elem2 for elem1, elem2 in zip(row1, row2)] for row1, row2 in zip(mat1, mat2)]
