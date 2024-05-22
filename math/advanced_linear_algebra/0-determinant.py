#!/usr/bin/env python3
"""
This module provides a function to calculate the determinant of a matrix.
"""

def determinant(matrix):
    """
    Calculate the determinant of a matrix.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError()
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    if rows != cols:
        raise ValueError()
    
    if rows == 0:
        return 0
    
    if rows == 1:
        return matrix[0][0]
    
    determinant_value = 0
    
    for col in range(cols):
        submatrix = [[row[i] for i, r in enumerate(matrix[1:]) if i != col] for row in matrix[1:]]
        determinant_value += matrix[0][col] * determinant(submatrix) * (-1)**(col + 1)
    
    return determinant_value
