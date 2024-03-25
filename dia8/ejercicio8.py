#for each (Ciclo for)
"""
for variable in iterable:
    # se ejecutará código para cada valor del iterable.
    # El código debe estar correctamente tabulado.
"""

#Funcion range(), el ultimo numero no es considerado
#valor de inicio por default es 0 [0-10[
for i in range(10): #En este ejemplo se ocupa i pero puede ser lo que uno quiera escribir
    print(i) #0,1,2,3,4,5,6,7,8,9
    
print("--------------------")

# Se establece el valor de inicio [4-10[
for i in range(4,10):
    print(i) #4,5,6,7,8,9
print("--------------------")

# El tercer valor corresponde a la frecuencia [4-10[
for i in range(4,10,2):
    print(i) #4,6,8

print("------ ejercicio traer numero par ------")

for i in range(0,21,2):
    print(i)

print("--------------------")

for i in range(1,21,2):
    print(i+1)

""" Otra forma de realizar lo anterior pero menos eficiente con validación
for num in range(1,21):
    if num % 2 == 0:
        print(num)
"""

print("------ Con while asegurandose que sea par ------------")
contador = 1
while contador <= 20:
    if contador % 2 == 0:
        print(contador)
    contador+=1

print("------ Otra con while pero pq conozco mi valor de inicio ------------")#Como se que mi contador parte en 0 puedo agregarle 2 en 2
contador = 0
while contador <= 20:
    print(contador)
    contador+=2


#LISTAS ITERABLES
#lista: Conjunto de datos, pueden ser numeros, strings, otra lista, etc.. Ordenados segun su ingreso, separados por coma
#El primer elemento esta en la posición 0 -> Posición 0: [1] Posición 1: [5] Posición 2: [8]..
lista = [1,5,8,3,4,]
print("--------------- Listas -----------")
for elemento in lista: #Se le asigna a elemento = los elementos de la lista en su orden
    print(elemento) 

print("--------- Listas String -----------")
#String -> Los string son considerados como un objeto iterable
texto = "Hola mundo!!"
for caracter in texto:
    print(caracter)

#Ejemplo con strings pero que tome todo el texto
#Tamaño de la lista es la cantidad de elementos
opciones = ['piedra','papel','tijera']
for opcion in opciones:
    print(opcion)

#DICCIONARIO { clave: valor, }
#En los diccionarios no existen las posiciones

diccionario = {
    "Nombre": "Carlos",
    "Apellido": "Santana",
    "Ocupación": "Guitarrista"
}

print("--------- Diccionario -----------")

for clave in diccionario:
    print(clave)

for clave in diccionario:
    print(f"clave: {clave} - valor: {diccionario[clave]}")
    #print(clave)
    #print(diccionario[clave])
    
print("---------  -----------")
for valor in diccionario.values():
    print(f" El valor es {valor}")

print("---------  -----------")
for clave, valor in diccionario.items():
    print(f"clave: {clave} - valor: {valor}")

