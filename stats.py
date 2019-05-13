import csv
import numpy as np
import pandas as pd

# Prints summary stats for Venezuelan GDP 1970-2017
datapath = './data/Per capita GDP at current prices - US dollars.csv'
df = pd.read_csv(datapath, header=0)
df = df.sort_values('Year', ascending=True)
df = df[df['Country or Area']=='Venezuela (Bolivarian Republic of)']
df = df[['Year', 'Value']]
series = pd.Series(df['Value'], index=df['Year'])
print(df.pct_change(axis='rows').describe())

# Prints summary stats for Venezuelan GDP 1999 - 2013
df2 = df[df['Year'] >= 1999]
df2 = df2[df2['Year'] <= 2013]
print(df2.pct_change(axis='rows').describe())

# Prints summary stats for Venezuelan GDP 2013 - 2017
df3 = df[df['Year'] >= 2013]
print(df3.pct_change(axis='rows').describe())
