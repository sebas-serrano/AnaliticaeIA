import pandas as pd

# Cargamos un archivo con pandas
df = pd.read_csv("archivos/03 characters.csv")

#print(df.head())
print(df.info())

#print(df.columns)
print(df ['height'].min())

a = df [['species','height']]
print(a)
b= a.groupby('species').sum().sort_values('height', ascending=True)
print(b)