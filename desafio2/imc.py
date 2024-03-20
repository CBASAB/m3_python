#Captura de datos
peso_kilos = float(input("Ingrese su peso en Kg: \n"))
altura = float(input("Ingrese su altura en metros: \n"))

#Print de datos
indice_masa_corporal = float(peso_kilos/altura**2)
print("Su Indice de Masa Corporal IMC es: ", peso_kilos/altura**2)

if indice_masa_corporal < 18.5:
    print("La clasificación OMS es Bajo Peso")
elif 18.5 <= indice_masa_corporal and indice_masa_corporal <25:
    print("La clasificación OMS es Adecuado")
elif 25 >= indice_masa_corporal and indice_masa_corporal <30:
    print("La clasificación OMS es Sobrepeso")
elif 30 >= indice_masa_corporal and indice_masa_corporal <35:
    print("La clasificación OMS es Obesidad Grado I")
elif 35 >= indice_masa_corporal and indice_masa_corporal <40:
    print("La clasificación OMS es Obesidad Grado II")
elif 40 >= indice_masa_corporal:
    print("La clasificación OMS es Obesidad Grado III")