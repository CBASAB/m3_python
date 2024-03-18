#Captura de datos
precio = int(input("Ingrese el precio del servicio en CLP: \n"))
cantidad_usuarios = int(input("Ingrese la cantidad de usuarios: \n"))
gastos_totales = int(input("Ingrese la cantidad de gastos totales en CLP: \n"))
utilidades_anio_anterior = int(input("Ingrese las utilidades del año anterior en CLP (Mayores a 0): \n"))

#Se realiza Calculo
utilidades_actuales = (precio * cantidad_usuarios) - gastos_totales
razon_utilidad_actual_y_anterior = (utilidades_actuales / utilidades_anio_anterior)

#Print de datos
print(f"La razón entre la utilidad actual vs la utilidad del año anterior es: {round(razon_utilidad_actual_y_anterior,2)} de crecimiento")

