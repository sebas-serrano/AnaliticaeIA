import numpy as np

"""
Siendo:
A X1 + B X2 = c
D X1 + E X2 = F

Despejamos X1 y X2
x2 = ( c - A X1 ) / B
X1 = (F - E X2 ) /D

Reemplazamos X1 en la funcion de X2
x2 = ( c - A ((F - E X2 ) /D) ) / B

Despejamos
X2 = (CD - AF) / (AE + BD)
"""

# A, B,C,D,E y F los debe ingresar el usuario

def calcularEcuaciones(a, b, c, d, e, f):
    """
    Funcion calcular los valores de X1 y de X2.

    Args:
       a, b, c, d, e, f (int)      
    
    Returns:
       Los valores de X1 y X2
    """

    print("Calculamos el valor de X2: ")
    denominador = (b * d - a * e)
    if denominador == 0:
        print("Error: el sistema no tiene solución única (división por cero).")
        return

    X2 = (c * d - a * f) / denominador
    print("El valor de X2 es: ",X2)
    
    print("Calculamos el valor de X1: ")
    X1 = (f - e * X2 ) / d
    print("El valor de X1 es: ",X1)

def cargarDatos():
    a = float(input("A: "))
    b = float(input("B: "))
    c = float(input("C: "))
    d = float(input("D: "))
    e = float(input("E: "))
    f = float(input("F: "))
    return a, b, c, d, e, f

# Programa principal
a, b, c, d, e, f = cargarDatos()
calcularEcuaciones(a, b, c, d, e, f)