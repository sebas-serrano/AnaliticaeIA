try:
    numero = int(input("Ingresa un número: "))
    resultado = 10 / numero
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Error: División por cero.")
except ValueError:
    print("Error: Debes ingresar un número válido.")
finally:
    print("Ejecución completada.")