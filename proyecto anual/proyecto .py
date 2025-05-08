import sqlite3
import pandas as pd

# Conexión a la base
conn = sqlite3.connect('C:/Users/User/iCloudDrive/Cursos/UTEC/Trabajo Integrador/Inmobiliaria/meliapi_data.sqlite')

# Lista de nombres de las tablas
nombres_tablas = ['APIDATA_MLU1466', 'APIDATA_MLU1467', 'APIDATA_MLU1468', 'APIDATA_MLU1472']

# Lista para acumular los DataFrames
dataframes = []

# Leer cada tabla y guardarla en la lista
for nombre in nombres_tablas:
    print(f"Leyendo tabla: {nombre}")
    df = pd.read_sql(f"SELECT * FROM {nombre}", conn)
    df["tabla_origen"] = nombre  # opcional: para saber de dónde vino cada fila
    dataframes.append(df)

# Unir todo en un único DataFrame
df_unificado = pd.concat(dataframes, ignore_index=True)

# Mostrar resultado
print(f"Total de filas combinadas: {len(df_unificado)}")
print(df_unificado.head(10))


