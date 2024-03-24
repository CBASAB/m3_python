import time
import sys
i = int(sys.argv[1])# Fijar valor inicial
# El ciclo terminara cunado i sea 0
while i > 0:
    print (i)
    time.sleep(1) #Espera 1 segundo
    i -= 1 # i ira decreciendo en 1 unidad.

print("BOOM!") #Al salir del ciclo la bomba explota!!
