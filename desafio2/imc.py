#Captura de datos y validación
peso_kilos = float(input("Ingrese su peso en Kg: \n"))
if peso_kilos <= 0:
    peso_kilos = float(input("Su peso no puede ser 0. Reingrese su peso en Kg: \n"))
altura = float(input("Ingrese su altura en cm: \n"))
if altura <= 0:
    altura = float(input("Su altura no puede ser 0. Reingrese su altura en cm: \n"))

#Conversión de centimetros a metros
altura = float(altura/100)

#Print de datos
indice_masa_corporal = float(peso_kilos/altura**2)
print(f"Su Indice de Masa Corporal IMC es: {round(indice_masa_corporal,2)}")

#Condiciones
if indice_masa_corporal < 18.5:
    print("La clasificación OMS es Bajo Peso")
elif indice_masa_corporal < 25:
    print("La clasificación OMS es Adecuado")
elif indice_masa_corporal < 30:
    print("La clasificación OMS es Sobrepeso")
elif indice_masa_corporal < 35:
    print("La clasificación OMS es Obesidad Grado I")
elif indice_masa_corporal < 40:
    print("La clasificación OMS es Obesidad Grado II")
else:
    print("La clasificación OMS es Obesidad Grado III")