import numpy as np

arr = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# 1)
totalSize = arr[1:,7].size
sucessosSize = np.count_nonzero(arr[1:,7] == 'Success')
print(totalSize)
print(sucessosSize)
print((sucessosSize/totalSize)*100, '%')

# 2)
floatCol = arr[1:,6].astype(float)
sizeCost = np.count_nonzero(floatCol)
sumCol = np.sum(floatCol)
print(sumCol/sizeCost)

# 3)
cond = np.char.count(arr[1:,2], 'USA')
countUSAMissions = np.count_nonzero(cond)
print("Missões realizadas pelos EUA:",countUSAMissions)

# 4)
arrSpaceXMissions = arr[arr[:,1] == 'SpaceX']
arrExpensiveMission = np.max(arrSpaceXMissions[1:,6].astype(float))
cond = arrSpaceXMissions[1:,6].astype(float) == arrExpensiveMission
print ("O ID da viagem mais cara da SpaceX é:",arrSpaceXMissions[1:,0][cond])

#5)
arrEmpresas, arrCount = np.unique(arr[1:,1], return_counts=True)
for i in range(arrEmpresas.size):
    print(arrEmpresas[i],":",arrCount[i])
 