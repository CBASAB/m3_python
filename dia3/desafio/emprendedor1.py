#Captura de datos
precio = int(input("Ingrese el precio del servicio en CLP: \n"))
cantidad_usuarios = int(input("Ingrese la cantidad de usuarios: \n"))
gastos_totales = int(input("Ingrese la cantidad de gastos totales en CLP: \n"))

#Se realiza calculo
utilidades = precio * cantidad_usuarios - gastos_totales

#Impresion
print(f"Las utilidades son: ${utilidades}")
