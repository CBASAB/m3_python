#Se importan librerias
import getpass
from string import ascii_lowercase

#Se solicita a usuario escribir una contraseña, ocultamos su escritura con getpass y la transformamos a minúscula.
contrasenia = getpass.getpass("Ingrese la contraseña (solo letras): \n").lower()

#Se establece contador de intentos
cantidad_intentos = 0

#Comienza ciclo for
for cantidad_letra in contrasenia:
    for letra in ascii_lowercase:
        cantidad_intentos += 1
        if cantidad_letra == letra:
            break

#Impresión
print(f"La contraseña fue forzada en {cantidad_intentos} intentos")