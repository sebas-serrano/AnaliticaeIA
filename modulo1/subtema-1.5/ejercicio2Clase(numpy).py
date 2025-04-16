import numpy as np

# Crear matriz vacía
defectuoso = [0.02, 0.05, 0.08, 0.1]
tipos = ['Transparentes','Opacos']

datos = np.zeros((2, 4), dtype=int)

def cargarDatos():
    global datos
    # Cargar datos
    for i in range(2):
        print("Ingrese los valores del tipo: ", tipos[i])
        for j in range(4):
            valor = int(input(f"Ingrese el valor para la posición [{i}][{j}]: "))
            datos[i][j] = valor

cargarDatos()
print(datos[1,2])

        
