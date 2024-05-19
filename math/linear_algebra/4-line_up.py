#!/usr/bin/env python3
"""
Module for adding arrays element-wise.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Parameters:
    arr1 (list): The first array.
    arr2 (list): The second array.

    Returns:
    list: A new list containing the result of adding corresponding elements
    If the lengths of arr1 and arr2 are different, 
	returns None.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
