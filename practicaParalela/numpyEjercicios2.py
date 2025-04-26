"""
Atributos de un array
Existen varios atributos y funciones que describen las características de un array.

"""

import numpy as np
a1 = np.ones(4)
print(a1)
a2 = np.ones([4,3])
print(a2)
a3 = np.ones([4,3,8])
print(a3)

# a.ndim : Devuelve el número de dimensiones del array a.
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

# a.shape : Devuelve una tupla con las dimensiones del array a.
print(a1.shape)
print(a2.shape)
print(a3.shape)

# a.size : Devuelve el número de elementos del array a.
print(a1.size)
print(a2.size)
print(a3.size)

# a.dtype: Devuelve el tipo de datos de los elementos del array a.
print(a1.dtype)
print(a2.dtype)
print(a3.dtype)


###############################################################################################
a4 = np.linspace(1,40,19)
print(a4 [3])

print("---------------------------")
a5 =  np.ones([3,3])
for i in range(3):
    for j in range (3):
        a5 [i][j] = i*3+j
print(a5)
a6 =  np.ones([3,3])
for i in range(3):
    for j in range (3):
        a6 [i][j] = j*3+i+7

print(a6)
print(a6.dot(a5))


