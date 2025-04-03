"""
Objetivo: Definir 2 preguntas sobre el archivo que bajamos de https://www.kaggle.com/

DataSet: India Agriculture Crop Production
Link: https://www.kaggle.com/datasets/pyatakov/india-agriculture-crop-production?select=India+Agriculture+Crop+Production.csv
Contiene: 345.000 Registros Aprox

 Preguntas:
 1.- Cual fue el area (en has) que mas se semrbo y en que año fue.
 2.- Cual fue el Estado que mas produccion tuvo y cual fue el cultivo
 3.- 

"""

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
file = apertura_archivo()
anio_mas_sembrado(file)

