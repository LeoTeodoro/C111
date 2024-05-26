import pandas as pd
import numpy as np

df = pd.read_csv('cap5/paises.csv', delimiter=';')

#1. a) 
# oceania = df[df['Region'].str.contains('OCEANIA')]
# print(oceania['Country'])
# #b)
# print(oceania['Country'].count())

#2
# meanLiteracy = df['Literacy (%)'].mean()
# print(meanLiteracy)

#3
# maxPop = df['Population'].max()
# countryMaxPop = df[df['Population'] == maxPop]
# print(countryMaxPop.loc[:,['Country','Region']])

#4
noCoastCountry = df[df['Coastline (coast/area ratio)'] == 0]
noCoastCountry.to_csv('cap5/noCoast.csv', sep=';', header=False)