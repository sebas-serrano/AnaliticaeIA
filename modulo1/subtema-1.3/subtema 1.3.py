# USO DEL FOR
"""
Escribe una funcion dibuja_linea que reciba como parámetro un caracter y una cantidad (que es un numero entero). 
La funcion debe mostrar en la pantalla el caracter tantas veces como diga la variable cantidad.
•
Pideal usuarioun númeroenteropositivoy escribe tresfuncionesdiferentesque dibujen:
•
Un cuadradode n x n
•
Un triánguloque iniciecon un solo * y vayaaumentandouno másencadarenglónhasta alcanzarn
•
Una pirámide, que seríaelmismotriánguloperocentrado

"""

valor = int(input("Ingrese el numero: "))

def dibuja_cuadrado(caracter, n):
    print("\nCUADRADOS")
    for i in range(n):
        for j in range(n):
            print(caracter, end=" ")
        print()

def dibuja_triangulo(numero):
    print("\nTRIANGULOS")
    for i in range (numero+1):
      print("*" *i)  

def dibuja_piramide(numero):
    print("\nPIRAMIDES")  
    for i in range (numero+1):
        print(" " * (numero - i) + "*" * (2 * i - 1))
  
dibuja_cuadrado("A", valor)
dibuja_triangulo(valor)
dibuja_piramide(valor)