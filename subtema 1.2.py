import math

# Definición de una función con un parámetro
def saludar(nombre):
    print(f'Hola \033[35m{nombre}\033[0m')

# Llamadas a la función
saludar('Rosa')
saludar('Vanina')
saludar('Gustavo')
saludar('Bruno')
saludar(255)

# Definición de una función con más de un parámetro
def sumar(a, b, c):
    return a + b + c

# Llamadas a la función
print(sumar(4, 2, 3))
print(sumar(50, 20, 30))
print(sumar(1000, 200, 300))
print(sumar('hola', ' ', 'Santiago'))

# Definición de una función sin valor de retorno
def multiplicar(a, b):
    print(a * b)

# Llamadas a la función
multiplicar(4, 2)
multiplicar(50, 20)
multiplicar(1000, 200)
            
# Definición de una función sin valor de retorno
def multiplicar(a, b):
    return a * b

# Llamadas a la función
print(multiplicar(multiplicar(4, 2), multiplicar(3, 2)))
print(multiplicar('hola ', 3))
print(multiplicar(5, '* '))

# Crear una función que me calcule la hipotenusa
def calcular_hipotenusa(cateto_a, cateto_b):
    return math.sqrt(math.pow(cateto_a, 2) + math.pow(cateto_b, 2))

# Pedir catetos al usuario
cateto_a = float(input('Dame el valor del cateto a: '))
cateto_b = float(input('Dame el valor del cateto b: '))

# Llamar a la función
hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)

# Imprimir el resultado
print(f'La hipotenusa es de \033[34;1m{hipotenusa:.2f}\033[0m')
