"""
#Captura de datos
peso_kilos = float(input("Ingrese su peso en Kg: \n"))
altura = float(input("Ingrese su altura en cm: \n"))
#Conversión de centimetros a metros
altura = altura/100
"""
#Puedes importar libreria sys para ejecutar desde la terminal y no ocupar input
import sys
#Se ejecuta en la terminal: python dia7/ejercicio7.py 81 178
peso_kilogramos = float(sys.argv[1])
estatura = float(sys.argv[2])/100

print(sys.argv) #['dia7/ejercicio7.py', '81', '178']
print(sys.argv[1])#81
print(sys.argv[2])#178

#Calculo IMC
imc = peso_kilogramos/(estatura**2)
print(f"Tu IMC es de {imc:.2}")

#Podemos agregar una variable clasificacion para no repetir el mismo texto
if imc < 18.5:
    clasificacion = "Bajo Peso"
elif imc >=18.5 and imc < 25:
    clasificacion = "Adecuado"
elif imc < 30:
    clasificacion = "Sobrepeso"
elif imc < 35:
    clasificacion = "Obesidad Grado I"
elif imc < 40:
    clasificacion = "Obesidad Grado II"
else:
    clasificacion = "Obesidad Grado III"

print(f"La clasificación OMS es {clasificacion}")