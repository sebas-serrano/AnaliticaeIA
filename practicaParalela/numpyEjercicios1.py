import numpy as np

# np.empty(dimensiones) : Crea y devuelve una referencia a un array vacío con las dimensiones especificadas en la tupla dimensiones.
# Las crea con basura dentro, recomendable usar solo si se cargan con datos rapidamente.
a1 = np.empty(3)
print(a1)

# np.zeros(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos ceros.
a2 = np.zeros(3)
print(a2)

a3 = np.zeros([4,6])
print(a3)

# np.ones(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos unos.
a4 = np.ones(3)
print(a4)

a5 = np.ones([3,6])
print(a5)

# np.full(dimensiones, valor) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son todos valor.
a6 = np.full(3,50)
print(a6)

a7 = np.full([3,8],50)
print(a7)

# np.identity(n) : Crea y devuelve una referencia a la matriz identidad de dimensión n.
a8 = np.identity(4)
print(a8)

# np.arange(inicio, fin, salto) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia desde inicio hasta fin tomando valores cada salto.
a9 = np.arange(1,50,4)
print(a9)

# np.linspace(inicio, fin, n) : Crea y devuelve una referencia a un array de una dimensión cuyos elementos son la secuencia de n valores equidistantes desde inicio hasta fin.
a10 = np.linspace(1,50,5)
print(a10)

#  np.random.random(dimensiones) : Crea y devuelve una referencia a un array con las dimensiones especificadas en la tupla dimensiones cuyos elementos son aleatorios.
a11 = np.random.random(3)
print(a11)
