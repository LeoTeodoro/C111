import numpy as np

# 1)
np.random.seed(5)
arr = np.random.rand(10)
newArr = 100*arr
intArr = newArr.astype(int)
print(intArr)

# 2)
np.random.seed(10)
arr = np.random.randint(1,51,16)
mtz = arr.reshape(4,4)
print(mtz)

# 3)
mdCol = mtz.mean(axis=0)
print ("Media das colunas: ", mdCol)
print ("\nMaior media das colunas", mdCol.max())
mdLine = mtz.mean(axis=1)
print ("\nMedia das linhas", mdLine)
print ("\nMaior media das linhas", mdLine.max())

# 4)
unique = np.unique(mtz, return_counts=True)
print(unique)
print ("Números que se repetem duas vezes: ", unique[0][unique[1] == 2])