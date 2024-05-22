#!/usr/bin/env python3

def determinant(matrix):
    """
    Calculates the determinant of a square matrix.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError()
    
    n = len(matrix)
    if len(matrix[0]) != n:
        raise ValueError()
    
    if n == 0:
        return 1.0
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0.0
    for i in range(n):
        det += ((-1) ** i) * matrix[0][i] * determinant([row[:i] + row[i+1:] for row in matrix[1:]])
    
    return det
