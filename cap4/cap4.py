import numpy as np

"""
# NumPy Array
# 1-D
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

# 2-D
mtz = np.array([[1, 2], [3, 4]])
print(mtz)
print(type(mtz))

# Estruturando NumPy arrays
mtz = np.ones([5, 5])
print(mtz)

arr = np.zeros([10])
print(arr)

# arange
arr = np.arange(20, 30, 1).reshape(5, 2)  # Muda o formato da matriz
print(arr)
"""

# Operações com NumPy arrays
jan = np.arange(20, 30, 1)
fev = np.arange(40, 50, 1)
print(jan)
print(fev)
print(jan + fev)
print(np.concatenate([jan, fev]).reshape(5, 4))

# Tamanho de um ndarray
print(jan.size)
# Dimensão de um ndarray
print(jan.ndim)
# Shpae de um ndarray
print(jan.shape)
