"""
Falta agregar validación para que usuario no ingrese 0

"""



#Captura de datos
peso_kilos = float(input("Ingrese su peso en Kg: \n"))
altura = float(input("Ingrese su altura en cm: \n"))
#Conversión de centimetros a metros
altura = altura/100

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