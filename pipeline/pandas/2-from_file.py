#!/usr/bin/env python3
"""
Module to read a csv file
"""

import pandas as pd


def from_file(filename, delimiter):
    """
    Function to read a csv file
    Args:
        filename: the file to read
        delimiter: the column separator
    Returns: the data from the file as a pd.DataFrame
    """
    return pd.read_csv(filename, delimiter=delimiter)
