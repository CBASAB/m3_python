nombre = "Sebastian"
apellido1 = "Riveros"
apellido2 = "Aliaga"
edad = "34"
año = 2024 #es un numero
#Python no permite sumar letras con numeros
#Suma de string = concatenar
print ("****** Informacion *********")
print ("Tu nombre es " + nombre + "         **")
print ("Tu apellido paterno es " + apellido1 + "      **")
print ("Tu apellido materno es " + apellido2 + "      **")
print ("Tu tienes la edad de " + edad + "         **")
#Imprimiendo string y numeros en una misma linea
print ("el año es ", año, " mes",3," Dia",7)
print ("****************************")

edad = 34
direccion = "parcela 6"
edad = 21.5
edad = "50"

#Interpolacion de cadenas (otra forma de imprimir en un solo print) (f) print (f"")
mes = 3
dia = 7
#Dentro del string estoy poniendo los valores de las variables que cree
print (f"Hola {nombre}, El año es {año} del mes {mes} y el dia {dia}")

