import pandas as pd

df = pd.read_csv("archivos/05 country_vaccinations.csv")
print(df.head())
# print(df.describe())


# La cantidad de vacunas aplicadas en todo el mundo
vacunas_total = df ['total_vaccinations'].sum()
# print(vacunas_total)


# El promedio de vacunas DIARIAS aplicadas por país
promedio_pais = df.groupby('country')['daily_vaccinations'].mean()
# print(promedio_pais)


# La cantidad de vacunas aplicadas el día 29/01/21 en todo el mundo
df['date'] = pd.to_datetime(df['date'])
vacuna_enero = df [ df['date'] == "2021-01-29"] 
# print(vacuna_enero['total_vaccinations'].sum())


# La diferencia de vacunación entre los días 20/01/21 y 31/01/21 para México y EEUU


# ¿Cuántos países hay en la base de datos?
paises = df['country'].nunique()
# print(paises)

# ¿Cuántos países tienen información de vacunación en el continente Europeo?


# ¿Cuántas vacunas diferentes se han utilizado en la base de datos?

# ¿Cuántos países han utilizado la vacuna “Sputnik V”?

# ¿Cuáles son los 10 países con mayor porcentaje de personas totalmente vacunadas respecto a su población?

# ¿Cuáles son los 5 países con menor porcentaje de personas totalmente vacunadas respecto a su población?

