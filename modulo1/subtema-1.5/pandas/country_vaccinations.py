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

# ¿Cuántas vacunas diferentes se han utilizado en la base de datos?
vacunas = df['vaccines'].nunique()
# print(vacunas)

# ¿Cuántos países han utilizado la vacuna “Sputnik V”?
a = df[ df['vaccines'].str.contains('Sputnik V')]
# print(a ['country'].nunique())

# ¿Cuáles son los 10 países con mayor porcentaje de personas totalmente vacunadas respecto a su población?
# Primero elimino las filas que tengan 0
df = df[(df['people_vaccinated'] != 0) & (df['total_vaccinations'] != 0)]
mayor_porcentaje = df.groupby('country').agg({
    'total_vaccinations': 'sum',
    'people_vaccinated': 'sum'
})

mayor_porcentaje ['mayor_porcentaje'] = (mayor_porcentaje ['people_vaccinated'] / mayor_porcentaje ['total_vaccinations']) * 100
print(mayor_porcentaje.sort_values('mayor_porcentaje', ascending=False).head(10))

# Guardar todos los dataframe usados en formato de archivo de Excel

mayor_porcentaje.to_excel('vacunas.xlsx', sheet_name="vacunas2")

ExcelWriter -> writer
vacunas.to_excel(writer, 'vacunas.xlsx', sheet_name="vacunas")



