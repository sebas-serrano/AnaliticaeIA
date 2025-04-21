"""
Imprime la respuesta a las siguientes preguntas:
a.- ¿Cuál es la edad promedio de los empleados?
b.- ¿Hay más hombres o mujeres en la muestra?
"""

def abri_archivo():
    # Abrir un archivo con open() y close()
    file_handler = open('c:/Employees-1.csv')
     # Saltar el encabezado
    next(file_handler)
    return file_handler

def calcularPromedio(file_handler):
    # Saltar el encabezado
    #next(file_handler)

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

    # Mostrar resultados
    print("Sumatoria de Edad de toda la muestra:", edad_total)
    print("Cantidad total de empleados:", cantidad_empleados)
    if cantidad_empleados > 0:
        print("Promedio de edad de la muestra:", int(edad_total / cantidad_empleados))
    else:
        print("No hay datos válidos para calcular promedio.")
    
    # Cerramos el archivo
    file_handler.close()

def mayoriaMuestra(file_handler):
    cantidad_hombres = 0
    cantidad_mujeres = 0
    for linea in file_handler:
        lst = linea.strip().split(',')
        if lst[1] != 'NA' and lst[1] != '':
            try:
                genero = lst[1]
                if genero == "F":
                    cantidad_mujeres +=1                               
                else:
                    cantidad_hombres += 1
            except ValueError:
                continue 
    if cantidad_mujeres > cantidad_hombres:
        print(f"En la muestra hay mas mujeres que hombres con un total de {cantidad_mujeres} mujeres sobre {cantidad_hombres} hombres")
    else:
        print(f"En la muestra hay mas hombres que mujeres con un total de {cantidad_hombres} hombres sobre {cantidad_mujeres} mujeres")
 

file = abri_archivo()
calcularPromedio(file)
file = abri_archivo()
mayoriaMuestra(file)