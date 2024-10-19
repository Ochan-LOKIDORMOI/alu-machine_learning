#!/usr/bin/env python3

import pandas as pd
from_file = __import__('2-from_file').from_file

# Load the dataset
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Slice the DataFrame along the columns High, Low, Close, and Volume_BTC, taking every 60th row
# Print the last 5 rows of the resulting DataFrame
print(df[['High', 'Low', 'Close', 'Volume_(BTC)']].iloc[::60].tail())