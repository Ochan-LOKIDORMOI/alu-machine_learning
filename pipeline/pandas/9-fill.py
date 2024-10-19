#!/usr/bin/env python3

import pandas as pd

from_file = __import__('2-from_file').from_file

# Load the dataset
df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

df = df.drop(columns=['Weighted_Price'])

# Fill missing values in 'Close' with the previous row's value (forward fill)
df['Close'] = df['Close'].fillna(method='ffill')

# Fill missing values in 'High', 'Low', 'Open' with the corresponding row's 'Close' value
df['High'] = df['High'].fillna(df['Close'])
df['Low'] = df['Low'].fillna(df['Close'])
df['Open'] = df['Open'].fillna(df['Close'])

# Fill missing values in 'Volume_(BTC)' and 'Volume_(Currency)' with 0
df['Volume_(BTC)'] = df['Volume_(BTC)'].fillna(0)
df['Volume_(Currency)'] = df['Volume_(Currency)'].fillna(0)

# Print the first 5 and last 5 rows of the modified DataFrame
print(df.head())
print(df.tail())
