#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the dataset
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Transpose the DataFrame and sort it in reverse chronological order
# Print the last 8 rows
print(df.sort_index(ascending=False).transpose().tail(8))