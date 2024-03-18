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

