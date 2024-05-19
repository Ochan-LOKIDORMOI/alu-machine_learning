#!/usr/bin/env python3
""" Implements the add_matrices function
"""


def add_matrices(mat1, mat2):
    """ Adds two matrices together
    """
    mat1_shape = get_mat_shape(mat1)
    mat2_shape = get_mat_shape(mat2)

    same_shape = compare_matrix_shapes(mat1_shape, mat2_shape)

    if not same_shape:
        return None

    # This will only run if the matrices are the same shape
    return add(mat1, mat2)


def add(mat1, mat2):
    """ Function to recursively add matrices of the same shape.
    """
    if is_number(mat1[0]) and is_number(mat2[0]):
        # We add only if the elements of mat1 and mat2 are ints
        return [num1 + num2 for num1, num2 in zip(mat1, mat2)]
    else:
        return [add(nums1, nums2) for nums1, nums2 in zip(mat1, mat2)]


def is_number(element):
    """ Function to determine if a passed element is a number or not
    """
    return isinstance(element, int) or isinstance(element, float)


def get_mat_shape(matrix):
    """ Function to get the shape of a matrix
    """
    current_dimension = matrix
    shape = []

    while isinstance(current_dimension, list):
        shape.append(len(current_dimension))
        current_dimension = current_dimension[0]

    return shape


def compare_matrix_shapes(mat1, mat2):
    """ Function to compare the shape of two matrices
    """
    result = True

    for element1, element2 in zip(mat1, mat2):
        result = result and element1 == element2

    return result
