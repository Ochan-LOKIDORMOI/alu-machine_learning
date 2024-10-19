#!/usr/bin/env python3

from datetime import date
import matplotlib.pyplot as plt
import pandas as pd
from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

# Remove the Weighted_Price column
df.drop(columns=['Weighted_Price'], inplace=True)

# Rename Timestamp to Date
df.rename(columns={'Timestamp': 'Date'}, inplace=True)

# Convert the timestamp values to date values
df['Date'] = pd.to_datetime(df['Date'], unit='s')

# Set Date as index
df.set_index('Date', inplace=True)

# Fill missing Close values with the previous row's value
df['Close'].fillna(method='ffill', inplace=True)

# Fill missing High, Low, Open values with the same row's Close value
df['High'].fillna(df['Close'], inplace=True)
df['Low'].fillna(df['Close'], inplace=True)
df['Open'].fillna(df['Close'], inplace=True)

# Fill missing Volume_(BTC) and Volume_(Currency) with 0
df['Volume_(BTC)'].fillna(0, inplace=True)
df['Volume_(Currency)'].fillna(0, inplace=True)

# Filter data from 2017 onwards
df = df[df.index >= '2017-01-01']

# Resample the data to daily intervals and aggregate
df_daily = df.resample('D').agg({
    'High': 'max',
    'Low': 'min',
    'Open': 'mean',
    'Close': 'mean',
    'Volume_(BTC)': 'sum',
    'Volume_(Currency)': 'sum'
})

# Plotting
df_daily.plot(y=['Open', 'High', 'Low', 'Close', 'Volume_(BTC)', 'Volume_(Currency)'],
              figsize=(14, 7))
plt.title('Daily Cryptocurrency Data from 2017 Onwards')
plt.xlabel('Date')
plt.ylabel('Values')
plt.legend(loc='upper left')
plt.show()