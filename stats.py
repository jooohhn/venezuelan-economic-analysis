import csv
import numpy as np
import pandas as pd

datapath = './data/Per capita GDP at current prices - US Dollars.csv'
df = pd.read_csv(datapath, header=0)
df = df.sort_values('Year', ascending=True)
df = df[df['Country or Area']=='Venezuela (Bolivarian Republic of)']
df = df[['Year', 'Value']]

# Prints summary stats for Venezuelan GDP 1970-2017 (Table1)
print('-------------Venezuelan Per Capita GDP % Change, 1970-2017 (Current US Dollars)----------------')
print(df['Value'].pct_change(axis='rows').describe())
print('')
# Prints summary stats for Venezuelan GDP 1999 - 2013 (Table 1)
df2 = df[df['Year'] >= 1999]
df2 = df2[df2['Year'] <= 2013]
print('-------------Venezuelan Per Capita GDP % Change, 1999-2013 (Current US Dollars)----------------')
print(df2['Value'].pct_change(axis='rows').describe())
print('')
# Prints summary stats for Venezuelan GDP 2013 - 2017 (Table 1)
print('-------------Venezuelan Per Capita GDP % Change, 2013-2017 (Current US Dollars)----------------')
df3 = df[df['Year'] >= 2013]
print(df3['Value'].pct_change(axis='rows').describe())
print('')

# Prints summary stats for world GDP growth in 2017 (Table 2)
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
df = df.rename(columns={'2017': 'Value'})
print('------------- International Per Capita GDP % Change, 1970-2017 (Current US Dollars)----------------')
print(df.pct_change(axis='columns')['Value'].describe())
