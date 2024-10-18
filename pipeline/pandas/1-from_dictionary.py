#!/usr/bin/env python3

import pandas as pd


"""
    Function that creates a pd.DataFrame from a dictionary
    Args:
        data: dictionary from which you should create the pd.DataFrame
    Returns:
        The newly created pd.DataFrame
"""
# Create the dictionary with the specified columns
data = {
    'First': [0.0, 0.5, 1.0, 1.5],
    'Second': ['one', 'two', 'three', 'four']
    }

# Create the DataFrame with labeled rows
df = pd.DataFrame(data, index=['A', 'B', 'C', 'D'])