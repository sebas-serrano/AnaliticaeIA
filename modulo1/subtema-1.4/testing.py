import unittest

def suma(a, b):
    return a + b

def test_suma():
    assert suma(2, 3) == 5, "Error en la función suma con dos números positivos"
    assert suma(-1, 1) == 0, "Error en la función suma con un número negativo y uno positivo"
    assert suma(0, 0) == 0, "Error en la función suma con dos ceros"
    assert suma(10, -5) == 5, "Error en la función suma con un número positivo y uno negativo"

# test_suma()
# print("Prueba completada correctamente.")

def es_primo(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True


def test_es_primo():
    assert es_primo(2) == True, "Error en la función es_primo con número 2"
    assert es_primo(3) == True, "Error en la función es_primo con número 3"
    assert es_primo(4) == False, "Error en la función es_primo con número 4"
    assert es_primo(5) == True, "Error en la función es_primo con número 5"
    assert es_primo(6) == False, "Error en la función es_primo con número 6"

test_es_primo()
print("Prueba completada correctamente.")

import pdb

def invertir_texto(texto):
    resultado = ""
    for i in range(1,len(texto)+1):
        pdb.set_trace()
        resultado += texto[-i] 
    return resultado

#  cadena = "Pyt"
cadena = "abc"
print(invertir_texto(cadena))

