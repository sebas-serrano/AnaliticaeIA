import pandas as pd

# Realiza la lectura del archivo starships.csv
df = pd.read_csv("archivos/04 starships.csv")


# Muestra la estructura del dataframe que contiene los datos
# print(df.info())


# Imprimos primeros registros
# print(df.head())


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
# print(nave_mas_larga)


# Obtén los registros de las naves con más de 1000 tripulantes (cargo_capacity)
mayores = df[df['cargo_capacity'] > 100000]
# print(mayores)


# Obtén los registros de las naves con el menor hyperdrive_rating
menor = df.sort_values('hyperdrive_rating', ascending=True).head(10)
# print(menor)


# Obtén todos los registros que son del tipo “Starfighter” o que su “hyperdrive_rating” sea mayor a la del promedio de las naves
promedio_hyperdrive = df['hyperdrive_rating'].mean()
registros = df[ (df['starship_class'] == 'Starfighter') | (df['hyperdrive_rating'] > promedio_hyperdrive) ]
# print(registros)


# Obtén una columna nueva con la relación entre “cargo_capacity” y “crew”, piensa por ejemplo en cuanta capacidad se puede 
# manejar por persona
df['nueva columna'] = df['cargo_capacity'] / df['crew']
# print(df['nueva columna'])


# Obtén los registros que tengan datos faltantes para “max_atmosphering_speed” y guarda el dataframe, después en el dataframe 
# original cambia los datos faltantes por 0

# 1. Guardar los registros con datos faltantes en 'max_atmosphering_speed'
df2 = df[df['max_atmosphering_speed'].isnull()].copy()

# 2. En el dataframe original, reemplazar los NaN por 0
df['max_atmosphering_speed'] = df['max_atmosphering_speed'].fillna(0)

# 3. Ahora, en df2, si querés cambiar su columna, también podés hacer:
df2['max_atmosphering_speed'] = 0  # (opcional)

# Mostrar para verificar
print(df2['max_atmosphering_speed'])