#Se importan librerias
import sys
import random

#Se solicita a jugador ingresar opción a jugar como argumento y lo convertimos a minuscula de inmediato
opcion_jugador = sys.argv[1].lower()

#Realizamos validación
if(opcion_jugador =="piedra" or opcion_jugador == "tijera" or opcion_jugador == "papel"):
    print(f"Tu opción jugada es:  {opcion_jugador}")

    #random para que busque elija un valor aleatoriamente de un lista asignada
    opcion_maquina = random.choice(['piedra','papel','tijera'])
    print(f"La opcion del computador es: {opcion_maquina}")
    
    if opcion_jugador == opcion_maquina:
        print("Empate")
    elif (opcion_jugador == "piedra" and opcion_maquina == "tijera") or (opcion_jugador == "tijera" and opcion_maquina == "papel") or (opcion_jugador == "papel" and opcion_maquina == "piedra"):
        print("Jugador gana")
    else:
        print("El computador gana")

else:
    print("Argumento inválido: Debe ser piedra o papel o tijera")