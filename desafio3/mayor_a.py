#Se importan librerias
import sys 

umbral = int(sys.argv[1])

#Diccionario
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
#Diccionario vacio
mayor_umbral = {}

#Recorrer diccionario
for clave, valor in ventas.items():
    #print(f"clave {clave} - valor {valor}")
    if umbral < valor :
        mayor_umbral[clave] = valor

print(f"El nuevo diccionario es: {mayor_umbral}")
    

#Crear diccionario nuevo con compresion
mayor_umbral2 = {clave: valor for clave, valor in ventas.items() if umbral < valor }
print(f"El nuevo diccionario2 es: {mayor_umbral}")
    
    
"""
Como agregar elementos a un diccionario
ventas["lunes"] = 2000
print(ventas)
"""
