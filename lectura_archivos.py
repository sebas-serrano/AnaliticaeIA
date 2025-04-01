
# Abrir un archivo con open() y close()
file_handler = open('c:/crop_production.csv')

for linea in file_handler:
    print(linea)

file_handler.close()

# Abrir un archivo con with
with open('c:/planets.csv') as archivo:
    for linea in archivo:
        print(linea)