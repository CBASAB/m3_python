#condicional if

#Si se cumple la condicion (True), 
# entonces se ejecuta el codigo
#if condicion :
    #codigo a ejecutar (tabulado a la derecha)
    
edad = input("¿Que edad tienes?\n")#20 -> Se almacena "20"
edad = int(edad)# edad = int("20") -> edad = 20

#Si el usuario es mayor de edad o menor de edad
if edad >= 18:
    print("Eres mayor de edad")
print("Programa terminado")

#ELSE, para mas de una opcion como respuesta o respuesta que queda por default

#if condicion :
    #codigo a ejecutar (tabulado a la derecha)
#else:
    #(entonces) Ejecutar el siguiente codigo
    
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("Programa terminado2")