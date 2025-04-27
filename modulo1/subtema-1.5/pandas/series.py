import pandas as pd

# Crea una Serie llamada nombres que contenga los siguientes valores: 'Juan', 'Ana', 'Pedro', 'Luis' y 'Sofía'. Muestra la Serie.
serie_nombres = pd.Series(['Juan', 'Ana', 'Pedro', 'Luis','Sofía'])
# print(serie_nombres)


# A partir de la Serie creada en el ejercicio anterior, muestra cuántos elementos tiene la Serie.
# print("cantidad de elementos: ",serie_nombres.count())


# Crea una Serie con las edades correspondientes a los nombres anteriores: 28, 25, 30, 27, 24. Muestra la Serie
series_edad = pd.Series(['28', '25', '30', '27','24'])
# print(series_edad)


# Crea un DataFrame llamado personas a partir de las Series nombres y edades. El DataFrame debe tener dos columnas: "Nombre" y "Edad". Muestra el DataFrame.
personas = pd.DataFrame({
    "Nombre": serie_nombres,
    "Edad": series_edad
})
personas["Edad"] = personas["Edad"].astype(int)
# print(personas)


# Muestra sólo la columna "Nombre" del DataFrame personas.
# print(personas['Nombre'])


# Agrega una columna al DataFrame personas llamada "Ciudad" con los valores: 'Montevideo', 'Salto', 'Paysandú', 'Rivera', 'Maldonado'. Muestra el DataFrame resultante.
series_ciudad = pd.Series(['Montevideo', 'Salto', 'Paysandú', 'Rivera', 'Maldonado'])
personas ['Ciudad'] = series_ciudad
# print(personas)


# Muestra los datos de las personas cuya edad es mayor a 25 años.
mayor_veinticinco = personas [ personas['Edad'] > 25 ]
# print(mayor_veinticinco)


# Calcula la edad promedio de las personas.
promedio = personas['Edad'].mean()
# print("Edad promedio: ",promedio)


# Ordena el DataFrame personas por la columna "Edad" de menor a mayor.
# print (personas.sort_values('Edad', ascending=True))

# Crea un DataFrame llamado ventas con las siguientes columnas y valores:
# Producto: 'Lapicera', 'Cuaderno', 'Goma', 'Regla'
# Cantidad: 10, 5, 8, 12
# Precio: 25, 50, 20, 30
producto = pd.Series(['Lapicera', 'Cuaderno', 'Goma', 'Regla'])
cantidad = pd.Series([10, 5, 8, 12])
precio = pd.Series([25, 50, 20, 30])
ventas = pd.DataFrame({
    "Producto": producto,
    "Cantidad": cantidad,
    "Precio": precio
})
ventas["Precio"] = ventas["Precio"].astype(int)
ventas["Cantidad"] = ventas["Cantidad"].astype(int)
# print(ventas)


# Agrega una columna llamada "Total" que sea el resultado de multiplicar la cantidad por el precio de cada producto. Muestra el DataFrame actualizado.
ventas ['Total'] = ventas['Cantidad'] * ventas ['Precio']
# print(ventas)


# Muestra solo aquellos productos cuya cantidad sea mayor a 7.
# print( ventas[ ventas['Cantidad']  > 7] )


# Muestra el valor total de todas las ventas (suma de la columna "Total").
valor_total = ventas['Total'].sum()
# print ("Ventas total:",valor_total)


# Ordena el DataFrame ventas por la columna "Total" de mayor a menor.
# print( ventas.sort_values('Total',ascending=False))


# Crea una Serie llamada notas con los siguientes valores: 8, 7, 10, 5, 9, 6, 8. Muestra la Serie.
notas = pd.Series( [8, 7, 10, 5, 9, 6, 8])
# print(notas)


# Muestra cuántos alumnos aprobaron (nota mayor o igual a 6) y cuántos no aprobaron.
print("Aprobaron", (notas >= 6).sum())
print("No Aprobaron", (notas < 6).sum())


# Muestra la nota máxima, mínima y el promedio de la Serie notas.
print("Nota maxima:", notas.max())
print("Nota minima:", notas.min())
print("Nota promedio:", notas.mean())

