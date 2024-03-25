#Se importan librerias
import sys 

#Se solicita a usuario ingresar opción como argumento
umbral = int(sys.argv[1])

#Diccionario con ventas entregadas
ventas = {
    "Enero": 15000,
    "Febrero": 22000,
    "Marzo": 12000,
    "Abril": 17000,
    "Mayo": 81000,
    "Junio": 13000,
    "Julio": 21000,
    "Agosto": 41200,
    "Septiembre": 25000,
    "Octubre": 21500,
    "Noviembre": 91000,
    "Diciembre": 21000,
}

#Se crea diccionario vacio en el cual iran las ventas que superen el umbral
umbral_superado = {}

#Se recorre diccionario
for clave, valor in ventas.items():
    if umbral < valor :
        umbral_superado[clave] = valor

#Print
print(f"Los meses y sus valores que superan el umbral ingresado son: {umbral_superado}")

