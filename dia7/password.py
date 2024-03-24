"""
#Se importa libreria
import getpass

#getpass hace que no se escriba o vea la clave mientras uno la escribe
password = getpass.getpass("Ingresa el password:\n ")
#Ejemplo de print para mostrar lo que escribimos -> print(f"El password capturado {password}")

#hola -> es distinto a "hola mundo", por ende esta correcto, True y en este caso ejecuta error.
while password != "hola mundo":
    password = getpass.getpass("Error, Ingresa el password correcto nuevamente:\n ")

print("Clave correcta, Fin del programa")



numero = int(input("Ingrese un numero entero del 1 al 100:\n"))

while numero <1 or numero > 100:
    numero = int(input("Ingrese un numero entero del 1 al 100:\n"))

while numero != 33:
    numero = int(input("Ingrese un numero entero del 1 al 100:\n"))

print("Fin del programa")

"""

#while con contador
inicio = 0
fin = 6

while inicio < fin:
    print(f" inicio {inicio} , fin {fin}")
    inicio = inicio + 1

print("Fin del while")

#Contar (incremento de uno en uno)
contar = 0
contar = contar + 1
#Estas tres formas son lo mismo   i = i + 1 -> i +=1 -> i++
