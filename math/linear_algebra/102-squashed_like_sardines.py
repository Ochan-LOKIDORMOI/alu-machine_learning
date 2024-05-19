#!/usr/bin/env python3
""" Implements the cat_matrices method
"""
import numpy as np


def cat_matrices(mat1, mat2, axis=0):
    """ Concatenates two np.ndarray along the specified axis
    """
    return np.concatenate((mat1, mat2), axis)
