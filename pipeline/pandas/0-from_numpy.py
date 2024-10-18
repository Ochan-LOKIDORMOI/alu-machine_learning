#!/usr/bin/env python3

import pandas as pd
import string
import numpy as np


def from_numpy(array):
    """
    Function that creates a pd.DataFrame from a np.ndarray
    Args:
        array: np.ndarray from which you should create the pd.DataFrame
    Returns:
        The newly created pd.DataFrame
    """
# Get the number of columns in the array
    num_columns = array.shape[1]
    
    column_labels = list(string.ascii_uppercase[:num_columns])
    
    # Create and return the DataFrame
    return pd.DataFrame(array, columns=column_labels)
