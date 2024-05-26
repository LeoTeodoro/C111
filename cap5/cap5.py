import pandas as pd
import numpy as np

# Series
# dic = {'a':10, 'b':20, 'c':30}
# s = pd.Series(dic)
# print(s)
# s2 = pd.Series(data=[20, 30, 40],index=['b', 'c', 'd'])
# print(s + s2)
# print(s.add(s2, fill_value=0))#Soma elemento a elemento e preenche os valores faltantes com 0

# print(s['a'])
# print(s[['b','c']])

# print(s[s>10])

# DataFrame
# df = pd.DataFrame(
#     columns=['X', 'Y', 'Z'],
#     index=['A', 'B', 'C'],
#     data=np.random.randint(1,50,[3,3])
# )
# print(df)

#Slicing usando loc
# print(df.loc[['B','C'],['X','Y','Z']])
# print(df.iloc[1:,:])

#Ler um dataset no pandas
df = pd.read_csv('cap5/paises.csv', delimiter=';')
print(df)

#Apenas colunas
print(df.columns)

#Apenas a coluna paises
print(df['Country'])

#Apenas as 3 primeiras linhas
print(df.head(3))

#Apenas as 3 últimas linhas
print(df.tail(3))