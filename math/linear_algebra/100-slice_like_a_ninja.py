#!/usr/bin/env python3
""" Implements the np_slice method
"""

def np_slice(matrix, axes={}):
    """ Slices a matrix along specified axes and limits
    """
    result = matrix

    {}.items()

    for axis, slice_params in axes.items():
        # Extract the slice params
        start, end, step = extract_slice_params(slice_params)

        # Create indices to use to get data
        indices = list(range(start, end, step))

        # Get rows from start to end using step
        result = result.take(indices, axis)

    return result


def extract_slice_params(slice_tuple):
    start = end = step = None

    # If only one value has been provided, it is the end value
    if len(slice_tuple) == 1:
        end = slice_tuple[0] or -1

    # If two values have been provided, then they are the start and end values
    elif len(slice_tuple) == 2:
        start, end = slice_tuple[0] or 0, slice_tuple[1] or -1

    # If three values have been provided, then they are the start, end and stop values
    elif len(slice_tuple) == 3:
        start, end, step = slice_tuple[0] or 0, slice_tuple[1] or -1, slice_tuple[2] or 1
    
    return start, end, step
