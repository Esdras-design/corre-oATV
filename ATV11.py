import numpy as np
array = np.array([10, 20, 30, 40, 50])
print(array + 2)

#---------------------------------------------
print(array * 3)

#-----------------------------------------------

array2 = np.array([1, 2, 3, 4, 5])
print(array + array2)

#-----------------------------------------------

print("Média:", np.mean(array))
print("Desvo padrão:", np.std(array))

#-------------------------------------------------

print(array[array % 2 == 0])