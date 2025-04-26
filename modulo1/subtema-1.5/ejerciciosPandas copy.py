import pandas as pd

"""
andas Series
Es muy parecido a un array de una dimensión (o vector) de NumPy.

• Arreglo unidimensional indexado
• Búsqueda por índice
• Slicing
• Operaciones aritméticas
• Distintos tipos de datos
"""

serie = pd.Series([12,34,56,78])
# Mostramos que es lo que tiene
print(serie)

#Multiplicamos
print(serie*4)

#Creamos 
serie2 = (["asd",34, True, "Algo"])
print(serie2)


"""
Pandas DataFrame
Muy parecido a las estructuras matriciales trabajadas con NumPy.

• Estructura principal
• Arreglo de dos dimensiones
• Búsqueda por índice (columnas o filas)
• Slicing
• Operaciones aritméticas
• Distintos tipos de datos
• Tamaño variable
"""

salud = pd.DataFrame({
    "paciente": pd.Series(["1","2","3"]),
    "edad": pd.Series([2,3,4])

}) 
print(salud)

salud["paciente"].sum()

#Vemos que columnas tienen nuestro DataFrame
print(salud.columns)

