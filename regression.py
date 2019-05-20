import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Correlation coef for oil prices to GDP per caputa
dfOil = pd.read_excel('./data/Oil Prices.xls', dtype={
  'Date': int, 'Value': float})
dfOil = dfOil.rename(columns={'Date': 'Year', 'Value': 'Oil Price per Barrel (USD)'})

dfGdp = pd.read_csv('./data/Per capita GDP at current prices - US Dollars.csv', header=0)
dfGdp = dfGdp.sort_values('Year', ascending=True)
dfGdp = dfGdp[dfGdp['Country or Area']=='Venezuela (Bolivarian Republic of)']
dfGdp = dfGdp[['Year', 'Value']]
dfGdp = dfGdp.rename(columns={'Value': 'GDP per Capita (USD)'})


dfOil = dfOil.set_index('Year')
dfGdp = dfGdp.set_index('Year')

dfJoin = dfOil.join(dfGdp, on='Year', how='inner', lsuffix=' - Oil Price', rsuffix='- GDP per Capita')
print(dfJoin.corr(method='pearson'))

import seaborn as sns
sns.lmplot(x='Oil Price per Barrel (USD)',
                      y='GDP per Capita (USD)', data=dfJoin,fit_reg=True)
plt.show()

