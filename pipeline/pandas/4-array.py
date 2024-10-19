#!/usr/bin/env python3

import pandas as pd
import numpy as np 
from_file = __import__('2-from_file').from_file

# Load the dataset
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Select the 'High' and 'Close' columns
df = df[['High', 'Close']]

# Take the last 10 rows
last_10_rows = df.tail(10)

# Convert to numpy.ndarray
A = last_10_rows.to_numpy()

# Print the result
print(A)
