import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('cap6/space.csv', delimiter=';')

# Filtrando as empresas dos EUA e da China

us_china_df = df[df['Location'].str.contains('USA|China')]

# Contando o número de empresas dos EUA e da China
company_counts = us_china_df['Company Name'].unique()
us_count = len(us_china_df[us_china_df['Location'].str.contains('USA')])
china_count = len(us_china_df[us_china_df['Location'].str.contains('China')])

# Criando um gráfico de barras
countries = ['USA', 'CHN']
counts = [us_count, china_count]

plt.bar(countries, counts)
plt.xlabel('Country')
plt.ylabel('Number of Companies')
plt.title('Number of Space Companies in USA and China')
plt.show()