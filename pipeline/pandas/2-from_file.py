#!/usr/bin/env python

"From File"

import pandas as pd


def from_file(filename, delimiter):
    # Use pandas' read_csv to load the data with the specified delimiter
    return pd.read_csv(filename, delimiter=delimiter)
