import numpy as np

arreglo1 = 0
arreglo2 = 0

def ingresoDatos():

    global arreglo1, arreglo2

    fila = int(input("Ingrese la cantidad de filas de la matriz: "))
    columna = int(input("Ingrese la cantidad de columnas de la matriz: "))

    print("La primer matriz es de: ", fila, " x ", columna)
    print("La segunda matriz es de: ", columna, " x ", fila)

    # Crear matriz vacía
    arreglo1 = np.zeros((fila, columna), dtype=int)

    # Cargar datos
    print("Ingrese los valores de la primera matriz:")
    for i in range(fila):
        for j in range(columna):
            valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            arreglo1[i][j] = valor

    # Crear segunda matriz para multiplicar
    arreglo2 = np.zeros((columna, fila), dtype=int)
    print("Ingrese los valores de la segunda matriz:")
    for i in range(columna):
        for j in range(fila):
            valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            arreglo2[i][j] = valor

def multiplicar():
    global arreglo1, arreglo2

    # Multiplicar matrices
    resultado = np.dot(arreglo1, arreglo2)

    # Mostrar resultado
    print("Resultado de la multiplicación:")
    print(resultado)

ingresoDatos()
multiplicar()