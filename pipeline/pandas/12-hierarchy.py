#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the datasets
df1 = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# Set 'Timestamp' as the index for both DataFrames
df1 = df1.set_index('Timestamp')
df2 = df2.set_index('Timestamp')

# Filter both DataFrames for the range of timestamps from 1417411980 to 1417417980
df1_filtered = df1.loc[1417411980:1417417980]
df2_filtered = df2.loc[1417411980:1417417980]

# Concatenate the filtered DataFrames with keys
df = pd.concat([df2_filtered, df1_filtered], keys=['bitstamp', 'coinbase'])

# Sort the DataFrame by Timestamp to display rows in chronological order
df = df.sort_index()

# Print the resulting DataFrame
print(df)
