import numpy as np

arr = np.loadtxt('brands.csv',delimiter=';',dtype='str',encoding='utf-8')

#1)
print("\n1)")
arrBrandValueGoogle = arr[arr[:,0] == 'Google']
arrBrandValueGoogle2022 = arrBrandValueGoogle[:,9].astype(float)
arrBrandValueGoogle2021 = arrBrandValueGoogle[:,10].astype(float)
print("Valorizaçao da marca google de 2021 para 2022 em dolares: ", arrBrandValueGoogle2022 - arrBrandValueGoogle2021)

#2)
print("\n2)")
arrBrandGroup = np.char.count(arr[1:,0], 'Group')
arrBrandGroupSize = np.count_nonzero(arrBrandGroup)
print("Numero de marcas com a palavra 'Group' no nome: ", arrBrandGroupSize)

#3)
print("\n3)")
arrFirstFiveBrands = arr[1:6,:]
arrFirstFiveBrands2023 = arrFirstFiveBrands[:,9].astype(float) * 1.1
#Sem usar for:
print("Valor de mercado das marcas", arrFirstFiveBrands[:,0], "para 2023 em dol: ", arrFirstFiveBrands2023)
#Usando for para ficar bonito:
print("\nUsando for:")
for i in range(0,5):
    print("Valor de mercado da marca ", arrFirstFiveBrands[i,0], " para 2023 em dol: ", arrFirstFiveBrands2023[i])

#4)
print("\n4)")
arrBrandsFoundedByAndYear = arr[1:,:3]
cond = arrBrandsFoundedByAndYear[:,2].astype(int) > 2000
print("Marcas fundadas após os anos 2000", arrBrandsFoundedByAndYear[cond][:,0])

#5
print("\n5)")
arrYearsFounded = arr[1:, 2].astype(int)
uniqueYears = np.unique(arrYearsFounded)
yearCounts = np.bincount(arrYearsFounded)
mostCommonYear = np.argmax(yearCounts)

print("Anos em que empresas foram fundadas:", uniqueYears)
print("Ano em que mais empresas abriram as portas:", mostCommonYear)