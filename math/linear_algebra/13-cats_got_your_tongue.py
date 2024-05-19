#!/usr/bin/env python3
""" implements the np_cat function
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """ concatenates np.ndarrays along a given axis
    default axis is 0
    """
    return np.concatenate((mat1, mat2), axis)
