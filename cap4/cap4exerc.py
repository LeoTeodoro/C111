import numpy as np

# 1)
arrExerc1 = np.linspace(0, 1, 21)
print(arrExerc1)

# 2)
arrExerc2 = np.arange(0, 51, 2)
print(arrExerc2)
arrExerc2_2 = np.arange(52, 101, 2)
print(arrExerc2_2)
arr2_concatenado = np.concatenate([arrExerc2, arrExerc2_2])
print(arr2_concatenado)

# # 3)
arrExerc3 = np.flip(arr2_concatenado)
print(arrExerc3)

# 4)
arrExerc4 = np.ones([3, 4])
arrExerc4Reshape = arrExerc4.reshape(1, 12)
print(arrExerc4Reshape)

# 5)
lenLines = np.random.randint(1, 10)
lenColumns = np.random.randint(1, 10)
arrExerc5 = np.random.rand(lenLines, lenColumns)
arrExerc5Shape = arrExerc5.shape
print(arrExerc5Shape)
arrExerc5Mult = arrExerc5Shape[0] * arrExerc5Shape[1]
if arrExerc5Mult % 2 == 0:
    print("Vetor de tamanho par")
else:
    print("Vetor de tamanho ímpar")
