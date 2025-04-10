import numpy as np

# Numpy

print("Mi primer arreglo: ")
arreglo1 = np.array([1,2,3,4,5])

print("Sumamos los elementos: ",arreglo1.sum())
print("Dimension: ",arreglo1.ndim)
print("Forma: ",arreglo1.shape)
print("Tipo de Datos: ",arreglo1.dtype)


print("Mi segundo arreglo: ")
arreglo2 = np.array([1.4,2,3,4,5])
print("Tipo de Datos: ",arreglo2.dtype)

arreglo3 = np.arange(1,152,10)
print(arreglo3)

arreglo4 = np.linspace(0,2,8)
print(arreglo4)

arreglo6 = np.arange(1,31)
print(arreglo6)

arreglo7 = np.arange(1,31)
print(arreglo7)

c=  np.add(arreglo6,arreglo7)
print(c)

matriz1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriz1)

matriz2 = np.ones((4,6))
print(matriz2)

matriz3= np.arange(5,101,5).reshape(10,2)
print(matriz3)