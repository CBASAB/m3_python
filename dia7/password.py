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

"""

numero = int(input("Ingrese un numero entero del 1 al 100:\n"))

while numero <1 or numero > 100:
    numero = int(input("Ingrese un numero entero del 1 al 100:\n"))

while numero != 33:
    numero = int(input("Ingrese un numero entero del 1 al 100:\n"))

print("Fin del programa")
