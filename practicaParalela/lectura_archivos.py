
# Abrir un archivo con open() y close()
file_handler = open('c:/crop_production.csv')

for linea in file_handler:
    print(linea)

file_handler.close()

# Abrir un archivo con with
with open('c:/planets.csv') as archivo:
    for linea in archivo:
        print(linea)

# Recorrer un archivos
file_handler = open('c:/planets.csv')
next(file_handler)

minimo_rotacional = 100
nombre_planeta = ""

for linea in file_handler:
  l = linea.split(',')

  if l[0] != 'NA' and l[1] != 'NA' and l[2] != 'NA':
    # preguntamos si el elemento siguiente es menor al que tenemos guardado.
    nombre = l[0]
    periodo_rotacional = int(l[1])
    periodo_orbital = l[2]    
    
    if minimo_rotacional >  periodo_rotacional:      
      minimo_rotacional = periodo_rotacional
      nombre_planeta = nombre
    elif periodo_rotacional  == minimo_rotacional:
      nombre_planeta = nombre_planeta + " , " + nombre

print("El planeta con el menor periodo rotacional es: ",nombre_planeta, " ", minimo_rotacional)

file_handler.close()