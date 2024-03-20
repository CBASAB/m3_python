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
print()
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

print("Programa terminado2")

#ELIF, vuelve a realizar una evaluación y va entre el IF y el ELSE en caso de agregarse

#if condicion :
    #codigo a ejecutar (tabulado a la derecha)
#elif (otra condicion): 
    #Si se cumple esta nueva condicion se ejecuta el codigo
#else:
    #(entonces) Ejecutar el siguiente codigo
#edad== 18; edad>18; edad<18;
print()
if edad > 18:
    print("Tu edad es mayor a 18")
elif edad == 18:
    print("Tu edad es igual a 18")
else:
    print("Tu edad es menor a 18")

print("Programa terminado3")