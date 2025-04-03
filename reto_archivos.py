"""
Objetivo: Definir 2 preguntas sobre el archivo que bajamos de https://www.kaggle.com/

DataSet: India Agriculture Crop Production
Link: https://www.kaggle.com/datasets/pyatakov/india-agriculture-crop-production?select=India+Agriculture+Crop+Production.csv
Contiene: 345.000 Registros Aprox

 Preguntas:
 1.- Cual fue el area (en has) que mas se semrbo y en que año fue.
 2.- Cual fue el Estado que mas produccion tuvo
 3.- 

"""

def estado_mas_productivo(file_handler):
    produccion_maxima = 0
    estado = ""
    unidad = ""
    for linea in file_handler:
        l = linea.split(',')
        if l[7] != '':        
            produccion = float(l[7])
            if produccion_maxima < produccion:
                produccion_maxima = produccion
                estado = l[0]
                unidad = l[8]

    print("EL Estado que mas  sembro fue: ", estado, " y la cantidad fue: ", produccion_maxima, " ", unidad)

def apertura_archivo():
    # Lectura del Archivo
    file_handler = open('C:/Users/User/iCloudDrive/Cursos/UTEC/DataSets/India Agriculture Crop Production.csv')

    next(file_handler)
    # State,District,Crop,Year,Season,Area,Area Units,Production,Production Units,Yield

    return file_handler

def anio_mas_sembrado(file_handler):
    area_maxima = 0
    anio = 0
    for linea in file_handler:
        l = linea.split(',')
        if l[5] != '':        
            area = float(l[5])
            if area > area_maxima:
                area_maxima = area
                anio = l[3]

    print("EL año que mas se sembro fue: ", anio, " y la cantidad fue: ", area_maxima, " has.")

# Llamada a los metodos
file_siembra = apertura_archivo()
anio_mas_sembrado(file_siembra)

file_siembra = apertura_archivo()
estado_mas_productivo(file_siembra)

