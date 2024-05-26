import numpy as np

arr = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')

#1)
print(arr[1:,:4])

#2)
arrRegion = np.unique(arr[1:,1])
arrRegionSize = arrRegion.size
print("Numero de regiões diferentes:",arrRegionSize)
print(arrRegion)

#3)
literacyFloat = arr[1:, 9].astype(float)
literacySum = np.sum(literacyFloat)
totalCoutries = arr[1:, 0].size
print("Média de alfabetização:",literacySum/totalCoutries, "%")

#4)
arrNorthAmerica = np.char.count(arr[1:,1], 'NORTHERN AMERICA')
print("Numero de países na América do Norte:",np.count_nonzero(arrNorthAmerica))

#5)
arrSouthAmericaAndCaribean = arr[arr[:,1] == 'LATIN AMER. & CARIB    ']
arrMaxGDP = np.max(arrSouthAmericaAndCaribean[1:,8].astype(float))
cond = arrSouthAmericaAndCaribean[1:,8].astype(float) == arrMaxGDP
print("O nome do país com o maior GDP da América do Sul e Caribe é:",arrSouthAmericaAndCaribean[1:,0][cond])

