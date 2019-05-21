import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Correlation coef for oil prices to GDP per capita
dfOil = pd.read_excel('./data/Oil Prices.xls', dtype={'Date': int, 'Value': float})
dfOil = dfOil.rename(columns={'Date': 'Year', 'Value': 'Oil Price per Barrel (USD)'})

dfGdp = pd.read_csv('./data/Per capita GDP at current prices - US Dollars.csv', header=0)
dfGdp = dfGdp.sort_values('Year', ascending=True)
dfGdp = dfGdp[dfGdp['Country or Area']=='Venezuela (Bolivarian Republic of)']
dfGdp = dfGdp[['Year', 'Value']]
dfGdp = dfGdp.rename(columns={'Value': 'GDP per Capita (USD)'})

dfOil = dfOil.set_index('Year')
dfGdp = dfGdp.set_index('Year')
# print(dfGdp)
dfJoin = dfOil.join(dfGdp, on='Year', how='inner', lsuffix=' - Oil Price', rsuffix='- GDP per Capita')
print('------------------------------------------------------------------------------------------------')
print(dfJoin.corr(method='pearson'))
print('')

sns.lmplot(x='Oil Price per Barrel (USD)',y='GDP per Capita (USD)', data=dfJoin, fit_reg=True)
plt.savefig('./Oil Price to GDP per Capita')

# Correlation coef for GDP and inflation
dfGdp = pd.read_csv('./data/Per capita GDP at current prices - US Dollars.csv', header=0)
dfGdp = dfGdp.sort_values('Year', ascending=True)
dfGdp = dfGdp[dfGdp['Country or Area']=='Venezuela (Bolivarian Republic of)']
dfGdp = dfGdp[['Year', 'Value']]
dfGdp = dfGdp.rename(columns={'Value': 'GDP per Capita (USD)'})
dfGdp = dfGdp.set_index('Year')
dfInflation = pd.read_csv('./data/Inflation.csv', header=0)
dfInflation = dfInflation[dfInflation['Country Name']=='Venezuela, RB']  
dfInflation = dfInflation.set_index('Country Name')
obj = {'year': [], 'rate': []}
for index, row in dfInflation.iterrows():
  for year in range(2009, 2017):
    obj['year'].append(year)
    obj['rate'].append(row[str(year)])
dfInflation = pd.DataFrame(data={'Inflation rate %': obj['rate']}, index=obj['year'])
dfJoin = dfGdp.join(dfInflation, on='Year', how='inner')
print('------------------------------------------------------------------------------------------------')
print(dfJoin.corr(method='pearson'))
print('')
sns.lmplot(x='Inflation rate %',
                      y='GDP per Capita (USD)', data=dfJoin, fit_reg=True)
plt.savefig('./Inflation rate % to GDP per Capita')

# Correlation coef for GDP % change and infant mortality rate rate
dfGdp = pd.read_csv('./data/Per capita GDP at current prices - US Dollars.csv', header=0)
dfGdp = dfGdp.sort_values('Year', ascending=True)
dfGdp = dfGdp[dfGdp['Country or Area']=='Venezuela (Bolivarian Republic of)']
dfGdp = dfGdp[['Year', 'Value']]
dfGdp = dfGdp.rename(columns={'Value': 'GDP per Capita (USD)'})
dfGdp = dfGdp.set_index('Year')
dfMortality = pd.read_csv('./data/Infant Mortaility.csv', header=0)
dfMortality = dfMortality[dfMortality['Country Name']=='Venezuela, RB']
obj = {'year': [], 'deaths': []}
for index, row in dfMortality.iterrows():
  for year in range(1960, 2017):
    obj['year'].append(year)
    obj['deaths'].append(row[str(year)])
dfMortality = pd.DataFrame(data={'Infant deaths per 1,000 live births': obj['deaths']}, index=obj['year'])
dfJoin = dfGdp.join(dfMortality, on='Year', how='inner')
print('------------------------------------------------------------------------------------------------')
print(dfJoin.corr(method='pearson'))
print('')
sns.lmplot(x='Infant deaths per 1,000 live births',y='GDP per Capita (USD)', data=dfJoin, fit_reg=True)
plt.savefig('./Infant deaths per 1,000 live births rate % to GDP per Capita')
