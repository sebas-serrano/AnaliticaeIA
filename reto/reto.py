
"""
Reto: Análisis descriptivo sobre empleados
Objetivo:
- Calcular la edad promedio de los empleados.
- Determinar si hay más hombres o mujeres en la muestra.
Requisitos:
- No usar pandas, csv, numpy u otras librerías externas.
- Usar manejo de excepciones.
"""

def abri_archivo():
    """
    Este método abre el archivo CSV que contiene los datos de empleados.

    Args:
        No recibe argumentos.

    Returns:
        Retorna un manejador de archivo abierto (file handler) con el encabezado ya saltado.
    """
    file_handler = open('c:/Employees-1.csv')
    next(file_handler)  # Saltar encabezado
    return file_handler


def calcularPromedio(file_handler):
    """
    Este método calcula la edad promedio de los empleados presentes en el archivo.

    Args:
        file_handler: Objeto de archivo abierto, apuntando a un archivo CSV ya sin encabezado.

    Returns:
        No retorna ningún valor. Imprime por pantalla:
            - La suma total de edades válidas.
            - La cantidad total de empleados considerados.
            - La edad promedio redondeada.
    """
    edad_total = 0
    cantidad_empleados = 0

    for linea in file_handler:
        lst = linea.strip().split(',')
        if lst[2] != 'NA' and lst[2] != '':
            try:
                edad = int(lst[2])
                edad_total += edad
                cantidad_empleados += 1
            except ValueError:
                continue

    print("Sumatoria de Edad de toda la muestra:", edad_total)
    print("Cantidad total de empleados:", cantidad_empleados)
    
    try:
        promedio = round(edad_total / cantidad_empleados)
        print("Promedio de edad de la muestra:", promedio)
    except ZeroDivisionError:
        print("No hay datos válidos para calcular promedio.")

    file_handler.close()


def mayoriaMuestra(file_handler):
    """
    Este método determina si hay más hombres o mujeres en la muestra del archivo.

    Args:
        file_handler: Objeto de archivo abierto, apuntando a un archivo CSV ya sin encabezado.

    Returns:
        No retorna ningún valor. Imprime por pantalla qué género es mayoritario,
        incluyendo el caso en que la cantidad sea igual.
    """
    cantidad_hombres = 0
    cantidad_mujeres = 0

    for linea in file_handler:
        lst = linea.strip().split(',')
        if lst[1] != 'NA' and lst[1] != '':
            genero = lst[1]
            if genero == "F":
                cantidad_mujeres += 1
            elif genero == "M":
                cantidad_hombres += 1

    if cantidad_mujeres > cantidad_hombres:
        print(f"En la muestra hay \033[1mmás mujeres\033[0m que hombres con un total de \033[1m{cantidad_mujeres}\033[0m mujeres sobre \033[1m{cantidad_hombres}\033[0m hombres")
    elif cantidad_hombres > cantidad_mujeres:
        print(f"En la muestra hay \033[1mmás hombres\033[0m que mujeres con un total de \033[1m{cantidad_hombres}\033[0m hombres sobre \033[1m{cantidad_mujeres}\033[0m mujeres")
    else:
        print(f"En la muestra hay \033[1migual cantidad\033[0m de hombres y mujeres: \033[1m{cantidad_hombres}\033[0m")

# Llamadas principales
file = abri_archivo()
calcularPromedio(file)

file = abri_archivo()
mayoriaMuestra(file)
