"""
Determinar si un numero ingresado por el usuario es par o impar
Utilizaremos el modulo o el resto de dividir un numero *2
"""
#Paso1 se solicitan datos
numero = int(input("Ingrese el numero a evaluar:\n"))

#Paso2 Evaluar con las condicionales
if numero == 0:
    print("El numero ingresado es 0")
elif numero%2 == 0:
    print("El numero ingresado es par")
else:
    print("El numero ingresado es impar")


