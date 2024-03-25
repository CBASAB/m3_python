#Importamos librerias
import sys
import random

buscar = int(sys.argv[1]) # número a buscar
print(buscar,type(buscar))

lista_numeros = [1,2,3,4,5,6,7,8,9,0]
random.shuffle(lista_numeros) #RANDOM.SHUFFLE -> DESORDENAR LA LISTA

print(lista_numeros)

"""

posicion = 0
for numero in lista_numeros:
    
    if buscar == numero:
        print("Numero encontrado!!")
        print(f"La posición es: {posicion}")
        break #Salir del for
    posicion+=1 #Incrementar en 1
"""
# revisaremos cada elemento en la lista
# también llevamos registro de la posición en la que estamos
for position, elemento in enumerate(lista_numeros):
# Si el elemento es igual a lo que buscamos terminamos el ciclo
    if elemento == buscar:
        print("¡Elemento encontrado! Se terminará del ciclo")
        break
    else:
# Si es que no es el elemento buscado lo reportamos
        print("Elemento no encontrado")

print("Ha terminado el ciclo")
print(f'El elemento {buscar} se encontró en la posición {position}')
print(f'La lista mezclada es: {lista_numeros}')


print("Fin del programa")
