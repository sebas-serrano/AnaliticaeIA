import numpy as np

"""
En una línea de manufactura se fabrican dos tipos de focos: transparentes (T) y opacos (O). 
De cada tipo se hacen cuatro modelos M1, M2, M3 y M4. Se debe pedir al operador del programa 
que introduzca la cantidad de focos que se realizaron de cada tipo y modelo. 
Considerando que el porcentaje de focos defectuosos del 2% para el modelo 1, el 5% para el modelo 2, 
el 8% para el modelo 3 y 10% para el modelo 4, 
calcule lo siguiente: 
    a) La cantidad de focos transparentes en buen estado que se fabrican 
    b) La cantidad de focos opacos defectuosos que se fabrican 
    c) Cuál es el tipo y modelo de foco que más se produce en mal estado
"""

# Crear matriz vacía
datos = np.zeros((2, 4), dtype=float)

# Arreglo de los porcentajes defectuoso
defectuoso = [0.02, 0.05, 0.08, 0.1]

# Arreglo con los tipos de focod
tipos = ['Transparentes','Opacos']

# Arreglo con los modelos de focos
modelos = ['M1','M2','M3','M4']


def cargarDatos():
    """
        Este metodo carga los datos del usuario.

        Args:
            No tiene entradas.
        
        Returns:
            Retorna la matriz con los datos cargados.    
    """
    global datos
    # Cargar datos
    for i in range(2):
        print("Ingrese la cantidad del tipo: ", tipos[i])
        for j in range(4):
            valor = int(input(f"Ingrese la cantida de focos para el tipo {modelos [j]} [{i}][{j}]: "))
            datos[i][j] = valor


def ejercicioA():
    """
        Funcion: La cantidad de focos transparentes en buen estado que se fabrican.

        Args:
            La matriz con los datos cargados.
        
        Returns:
            Cantidad de Focos transparentes en buen estado.
        
    """
    global datos, defectuoso
    salida = np.zeros(4, dtype=float)
    for i in range (4):
        salida[i] = datos[0, i] - (defectuoso[i] * datos[0, i])
    return salida


def ejercicioB():
    """
    Funcion: La cantidad de focos opacos defectuosos que se fabrican

    Args:
        La matriz con los datos cargados.
    
    Returns:
        Cantidad de Focos opacos defectuosos.
    
    """
    global datos, defectuoso
    salida = np.zeros(4, dtype=float)
    for i in range (4):
        salida[i] = defectuoso[i] * datos[1, i]
    return salida

def ejercicioC():
    global datos, defectuoso, tipos, modelos

    # Creamos una matriz de defectuosos (2 filas, 4 columnas)
    matriz_defectuosos = np.zeros((2, 4), dtype=float)

    for i in range(2):
        for j in range(4):
            matriz_defectuosos[i, j] = datos[i, j] * defectuoso[j]
     # Buscar el índice del valor máximo
    indice_max = np.unravel_index(np.argmax(matriz_defectuosos), matriz_defectuosos.shape)
    tipo_max = tipos[indice_max[0]]
    modelo_max = modelos[indice_max[1]]
    cantidad_max = matriz_defectuosos[indice_max]

    # Mostrar resultado
    print(f"\nEl tipo y modelo que más se produce en mal estado es: {tipo_max}, modelo {modelo_max}")
    print(f"Cantidad de defectuosos: {cantidad_max}")



# Main principal
cargarDatos()

#Llamamos al primer ejercicio e imprimos el resultado
salidaA =ejercicioA()
print("Cantidad de Focos Transparentes en buen estado:")
for i in range(4):
    print("Del modelo ", modelos[i], " se fabricaron ", salidaA[i])

#Llamamos al segundo ejercicio e imprimos el resultado
salidaB =ejercicioB()
print("Cantidad de Focos Opacos defectuosos:")
for i in range(4):
    print("Del modelo ", modelos[i], " se fabricaron ", salidaB[i])

ejercicioC()
        
