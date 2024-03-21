#Se importan librerias
import sys

opcion_jugador = sys.argv[1].lower() #TIJERAS O tijeras o TiJerAs -> Pero igual lo cambiamos a minuscula

if(opcion_jugador !="piedra" and "tijeras" and "papel"):
    print("Argumento Invalido: Debe ser piedra o papel o tijeras")
else: #Ingreso valido de los parametros por parte del usuario
    print("Continua el programa")


