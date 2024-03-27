"""
Listas
Pueden contener distintos tipos de elementos
Son mutables
Se usan los [] para definir una variable de tipo lista
** Indice -> La posicion de los elementos

La primera posición siempre es 0
La ultima posicion esta dada por ultima_posicion = (cantidad_elementos - 1) o lista[-1]
Para acceder a los elementos utilizamos las posiciones; lista[posicion]
No existen indices sin elementos en Python

Los metodos con __nombre__, se les llama "magic, built-in o dunders"
"""

lista1 = [1,2,3,4]
print(f"La lista es: {lista1}")
print(f" Nueva lista {[5,"Hola Mundo",7]}")

colores = ["verde", "rojo", "rosa", "azul"]
#cuantos elementos tiene la lista colores: 4 -> El tamaño de la lista
#La ultima posición de esta lista es = 4-1 -> 3
print(colores[0])#verde
print(colores[1])#rojo
print(colores[2])#rosa
print(colores[3])#azul
#print(colores[4]) #IndexError: list out of range -> Este produce error, ya que esta fuera del indice de la lista.
print(colores[-1])#azul
print(colores[-2])#rosa
print(colores[-3])#rojo
print(colores[-4])#verde
#print(colores[-5]) #IndexError: list out of range -> Este produce error, ya que esta fuera del indice de la lista.
#

## METODOS ##
#print(colores.__dir__()) #Mostrar todos los metodos que contiene la lista

colores.append("amarillo")# .append() -> agregar un elemento al final de la lista
print(colores) #['verde', 'rojo', 'rosa', 'azul', 'amarillo']

#insert(indice, elemento) -> Agregar el elemento en una posicion especifica (aca como esta escrito seria en vez de indice)
# y si la posicion esta utilizada por otro elemento, este es desplazado una posicion mas
colores.insert(0, "blanco") 
print(colores) #['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo']

colores.insert(6, "negro") #agregar al final de la lista porque tenia elementos del 0 al 5
print(colores) #['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo', 'negro']

colores.insert(18, "cafe") # si el indice no existe, le asigna la ultima posicion (cuando agregamos en una posicion fuera del rango lo que hace es crearlo al final)
print(colores) #['blanco', 'verde', 'rojo', 'rosa', 'azul', 'amarillo', 'negro', 'cafe']

colores.insert(0, "cafe") #['cafe', 'blanco', 'verde', 'rojo', 'azul', 'amarillo', 'negro', 'cafe']


# .pop([indice]) -> Elimina un elemento dentro de la lista
colores.pop(3) #elimina la 3 posición, en este caso el rojo y desplaza los otros elementos para ocupar el espacio que quedo vacio
print(colores) # ['cafe', blanco', 'verde', 'rosa', 'azul', 'amarillo', 'negro', 'cafe']

# .remove() -> Elimina un elemento ESPECIFICO dentro de la lista
colores.remove("cafe") #Elimina un elemento especifico, pero el primero que encuentra de izquierda a derecha
print(colores) #['blanco', 'verde', 'rosa', 'azul', 'amarillo', 'negro', 'cafe']
#colores.remove("cafes") #ValueError: list.remove(x): x not in list

# .reverse() -> Invierte el orden de los elementos de una lista, pero de manera permanente
colores.reverse()
print(colores) #['cafe', 'negro', 'amarillo', 'azul', 'rosa', 'verde', 'blanco']
#Si vuelvo a imprimir como es permanente, sigue asi
print(colores) #['cafe', 'negro', 'amarillo', 'azul', 'rosa', 'verde', 'blanco']

# .sort() -> Ordena los elementos de una lista de manera ascendente/alfabetico por defecto
colores.sort()
print(colores) #['amarillo', 'azul', 'blanco', 'cafe', 'negro', 'rosa', 'verde']

# En las listas no se guarda una variable de esta forma de abajo
lista2 = lista1 #ESTO NO ES UN RESPALDO DE LA LISTA
lista3 = lista1.copy() # ESTO SI ES UN RESPALDO DE LA LISTA Y SIEMPRE ANTES DE HACER UN CAMBIO
lista4 = lista1[:] # ESTO SI ES UN RESPALDO DE LA LISTA Y SIEMPRE ANTES DE HACER UN CAMBIO (slice)
lista5 = list(lista1) # ESTO SI ES UN RESPALDO DE LA LISTA Y SIEMPRE ANTES DE HACER UN CAMBIO
lista7 = lista1 + []
lista8 = lista1 * 1

"""
En Python, cuando asignas una lista a otra variable utilizando el operador de asignación (=), 
estás creando una nueva referencia a la misma lista en la memoria, no una nueva lista. Por lo tanto, 
ambas variables (lista1 y lista2) apuntan a la misma ubicación de memoria, lo que significa que 
cualquier cambio realizado en una de las variables también afectará a la otra.
"""

print(lista2)
lista2.append(5)
print(f"lista 2 {lista2}")
print(f"lista 1 {lista1}")
print(f"lista 3 {lista3}")
print(f"lista 4 {lista4}")
print(f"lista 5 {lista5}")

# sorted(lista, reverse = True) -> Ordena descendente dependiendo si le pasamos un parametro, esto no es permanente

print(sorted(colores,reverse=True)) # ['verde', 'rosa', 'negro', 'cafe', 'blanco', 'azul', 'amarillo']
print(sorted(colores)) #['amarillo', 'azul', 'blanco', 'cafe', 'negro', 'rosa', 'verde']
print(colores) #['amarillo', 'azul', 'blanco', 'cafe', 'negro', 'rosa', 'verde']

# .index() -> Retorna el indice del elemento existente en la lista
print(colores.index('azul')) #1
print(colores.index('negro')) #4
# print(colores.index('pink')) # ValueError: 'pink' is not in list

# .clear() 
colores.clear() # Eliminar o vaciar todos los elementos de la lista
print(colores) # [] -> Lista vacia
print(len(colores)) # 0



## OPERACIONES ##

lista6 = [20,30,40,50]

lista_concatenada = lista1 + lista6
print(lista1) # [1, 2, 3, 4, 5]
print(lista6) # [20, 30, 40, 50]
print(lista7) # [1, 2, 3, 4]
print(lista8) # [1, 2, 3, 4]
print(lista_concatenada) # [1, 2, 3, 4, 5, 20, 30, 40, 50]
lista6.append(60)
print(lista_concatenada)

