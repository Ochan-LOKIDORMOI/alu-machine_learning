#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the datasets
df1 = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')
df2 = from_file('bitstampUSD_1-min_data_2012-01-01_to_2020-04-22.csv', ',')

# Set 'Timestamp' as the index for both DataFrames
df1 = df1.set_index('Timestamp')
df2 = df2.set_index('Timestamp')

# Filter the bitstamp data to include all rows up to and including timestamp 1417411920
df2_filtered = df2.loc[:1417411920]

# Concatenate the two DataFrames, adding keys 'bitstamp' and 'coinbase'
df = pd.concat([df2_filtered, df1], keys=['bitstamp', 'coinbase'])

# Print the resulting DataFrame
print(df)
