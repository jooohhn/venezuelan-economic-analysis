import csv
import numpy as np
import pandas as pd

# Prints summary stats for Venezuelan GDP 1970-2017 (Table1)
datapath = './data/Per capita GDP at current prices - US Dollars.csv'
df = pd.read_csv(datapath, header=0)
df = df.sort_values('Year', ascending=True)
df = df[df['Country or Area']=='Venezuela (Bolivarian Republic of)']
df = df[['Year', 'Value']]
print(df.pct_change(axis='rows').describe())

# Prints summary stats for Venezuelan GDP 1999 - 2013 (Table 1)
df2 = df[df['Year'] >= 1999]
df2 = df2[df2['Year'] <= 2013]
print(df2.pct_change(axis='rows').describe())

# Prints summary stats for Venezuelan GDP 2013 - 2017 (Table 1)
df3 = df[df['Year'] >= 2013]
print(df3.pct_change(axis='rows').describe())

# Prints summary stats for world GDP growth in 2017 (Table 2)
datapath = './data/Per capita GDP at current prices - US Dollars.csv'
df = pd.read_csv(datapath, header=0)
df = df[df['Year'] >= 2016]
df = df.dropna()
df = df[df.duplicated(subset=['Country or Area'], keep=False)]
obj = {'Country': [], '2016' : [], '2017' : []}
for index, row in df.iterrows():
    if row['Country or Area'] not in obj['Country']:
      obj['Country'].append(row['Country or Area'])
    if row['Year'] == 2016:
      obj['2016'].append(row['Value'])
    if row['Year'] == 2017:
      obj['2017'].append(row['Value'])
df = pd.DataFrame(data={'2016': obj['2016'], '2017': obj['2017']}, index=obj['Country'])
print(df.pct_change(axis='columns'))
