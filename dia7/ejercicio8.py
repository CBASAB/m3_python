#Se importan librerias
import sys
import random

opcion_jugador = sys.argv[1].lower() #TIJERAS O tijeras o TiJerAs -> Pero igual lo cambiamos a minuscula

if(opcion_jugador !="piedra" and opcion_jugador != "tijeras" and opcion_jugador != "papel"):
    print("Argumento Invalido: Debe ser piedra o papel o tijeras")
else: #Ingreso valido de los parametros por parte del usuario
    print("Continua el programa")

if(opcion_jugador =="piedra" or opcion_jugador == "tijeras" or opcion_jugador != "papel"):
    print("Datos ingresados correctamente!!")

    print(f"La opcion de usuario es: {opcion_jugador}")

    #random -> Elije al azar de una lista
    opcion_maquina = random.choice(['piedra','papel','tijeras'])
    print(f"La opcion del computador es: {opcion_maquina}")
    
    if opcion_jugador == opcion_maquina:
        print("Empate")
    elif (opcion_jugador == "piedra" and opcion_maquina == "tijeras") or (opcion_jugador == "tijeras" and opcion_maquina == "papel") or (opcion_jugador == "papel" and opcion_maquina == "piedra"):
        print("Jugador gana")
    else:
        print("El computador gana")

else:
    print("Argumento Invalido: Debe ser piedra o papel o tijeras")
