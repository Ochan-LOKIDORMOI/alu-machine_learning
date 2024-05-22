#!/usr/bin/env python3

def determinant(matrix):
    """
    Calculate the determinant of a square matrix.
    """

    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if matrix is square
    if any(len(row) != len(matrix) for row in matrix):
        return 0

    # Base case for 0x0 matrix
    if len(matrix) == 0:
        return 1

    # Base case for 1x1 matrix
    if len(matrix) == 1:
        return matrix[0][0]

    # Recursive calculation for larger matrices
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col_idx, value in enumerate(matrix[0]):
        sign = (-1) ** col_idx
        sub_matrix = [row[:col_idx] + row[col_idx + 1:] for row in matrix[1:]]
        det += sign * value * determinant(sub_matrix)
    
    return det
