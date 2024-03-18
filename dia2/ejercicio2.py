#La separacion de los float es un punto (.)

#La division entre integers (Enteros), el resultado es un Float

print(4/2) #Aun cuando los numero son enteros el resultado sera un flotante 2.0
print(5/2) #2.5
print(5/3.5)
print(2.4*4) #Seguira siendo un flotante 9.6

nombre = "Seba"
año = "2024"
print(3*nombre) #Puedes multiplicar para que el contenido de la variable se repita
print(año*2) #20242024
#print(nombre/2) No se puede dividir un string

#Interpolacion de cadenas (otra forma de imprimir en un solo print) (f) print (f"")
mes = 3
dia = 7

#Dentro del string estoy poniendo los valores de las variables que cree
print (f"Hola {nombre}, El año es {año} del mes {mes} y el dia {dia}")

#string.format
#print("".format())
print("Hola {}, El año es {} del mes {} y el dia {}".format(nombre,año,mes,dia))

#Antigua forma de escribir lo mismo que arriba (Interpolacion con %).. %s es con string y %d es valor numerico
print("Hola %s, El año es %s del mes %d y el dia %d" %(nombre,año,mes,dia))

#Metodo .count Sirve para buscar y contar un caracter dentro de un string (Cuantas veces se encuentra)
print("Saitama".count("a")) #3 a
print(nombre.count("e")) # De mi nombre Seba hay una sola e

#Metodos upper y lower -> .upper() todo en mayuscula .lower() todo en minuscula
print("Saitama".upper())#SAITAMA Todo en mayuscula
print("SaItAmA".lower())#saitama todo en minuscula (A pesar de como lo escribi va a se va a mostrar en minuscula)
print(nombre.upper())#SAITAMA Todo en mayuscula
print(nombre.lower())#saitama todo en minuscula

#Metodo .title ->Deja la primera letra en mayuscula y el resto en minuscula (Si le agregas un numero antes igual sera la primera LETRA)
print("123saItAmA".title())#Saitama

apellido = "riveros"
print(apellido.title())#Otro ejemplo.. La variable estaba con minuscula y cambio la primera a mayuscula

# .len() -> Contar los caracteres de un string
print(len(" sebastian riveros 2024"))#tambien considera espacios

# .join() -> Unir string separados en un solo string
print(", ".join(["seba","riveros","aliaga"])) #En este caso el separador se definio como (, )

#Imprimir en mas de una linea (\n)
print("escribir\ncualquier\ncosas")
"""
escribir
cualquier
cosas
"""

mi_direccion = ""
miDireccion = ""
cantidad_alumnos = 30
peso = 85.5
verdadero = True

#Tipo de datos type(nombre_variable) Te dice al tipo de variable que pertenece
print(type(nombre))#<class 'str'>
print(type(año))#<class 'str'>
print(type(mes))#<class 'int'>
print(type(peso))#<class 'float'>
print(type(verdadero))#<class 'bool'>

type(verdadero)#no imprime el tipo de dato

#Manipulacion Variables

numero=2
numero=numero +3 #numero = 2 + 3
print(numero)#5

nombre = nombre + " Riveros" #nombre = "Seba"+" Riveros"
print(nombre) #Seba Riveros

#Precision de datos
print(5/9)
print(f"Resutlado de la division {5/9:.2f}") #Con dos decimales
print("el resultado de la division",round(5/9,3)) #Otra forma ocupando round(), y al final agregamos la cantidad de decimales, en este caso 3


nombre = input("Ingrese su nombre:  ")
print("Tu nombre es",nombre)
print(f"Tu nombre es {nombre}")

edad = input("Ingrese su edad:  ")
print("Tu tienes",edad,"años")
print(type(edad))#<class 'str'> Aun cuando el usuario ingresa una variable numerica lo transforma a string



