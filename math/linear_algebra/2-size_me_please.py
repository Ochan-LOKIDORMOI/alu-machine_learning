#!/usr/bin/env python3
"""
Module for calculating the shape of a matrix.
"""

def matrix_shape(matrix):
    """
    Calculates the shape of a matrix.

    Parameters:
    matrix (list): A list of lists (matrix) where each sublist is of the same length.

    Returns:
    list: A list of integers representing the shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
