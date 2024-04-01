import numpy as np

#NUMEROS ALEATORIOS
# random
# np.random.seed(10)
# arr = np.random.randint(1,11,15)
# print(arr)

#EXTRAINDO ELEMENTOS UNICOS
# print(np.unique(arr, return_counts=True))

#OPERACOES COM MATRIZES
# mtz = arr.reshape(3,5)
# print(mtz)
# print(mtz.sum(axis=1)[0])#axis=1 soma na horizontal

#BROADCASTING
# print(0.5*mtz)

#CONDICIONAIS
# print(mtz)
# cond = mtz%2==0
# cond2 = mtz>mtz.mean() 
# print(mtz[cond2])

#ANALISE TEXTUAL
#CHAR
# arr = np.array(['Pedro','Artur', 'Ana', 'Maciel'])
# result = np.char.find(arr, 'a') #MOSTRA A POSICAO EM QUE A LETRA SE ENCONTRA (CASE SENSITIVE)
# cond = np.char.find(arr,'a')>=0
# print(arr[cond])