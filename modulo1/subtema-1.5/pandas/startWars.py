import pandas as pd

# Realiza la lectura del archivo starships.csv
df = pd.read_csv("archivos/04 starships.csv")

# Muestra la estructura del dataframe que contiene los datos
# print(df.info())

# Imprimos primeros registros
print(df.head())

# ¿Cuál es el costo total de todas las naves que aparecen en el archivo de registro?
total = df['cost_in_credits'].sum() 
# print(total)

# ¿Cuál es el promedio de costos por fabricante?
promedio = df.groupby('manufacturer')['cost_in_credits'].mean()
# print(promedio)

# ¿Cuántas “starship_class” existen y cuáles son?
cantidad_clases = df['starship_class'].nunique()
# print("Existen", cantidad_clases, "starship_class distintas")

clases_unicas = df['starship_class'].unique()
# print("Las clases de starship_class son:", clases_unicas)


# ¿Cuál es la nave más barata?
fila_menor_costo = df.sort_values('cost_in_credits', ascending=True).head(1)
# print(fila_menor_costo)

idx = df['cost_in_credits'].idxmin()
nave_mas_barata = df.loc[idx]
# print(nave_mas_barata)


# ¿Cuál es la nave más larga?
idx_Larga = df['length'].idxmin()
nave_mas_larga = df.loc[idx_Larga]
print(nave_mas_larga)

# Obtén los registros de las naves con más de 1000 tripulantes





