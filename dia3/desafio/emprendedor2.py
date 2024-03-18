#Paso1: Captura de datos
precio_suscripcion = float(input("Ingrese el precio de suscripcion en CLP: \n"))
numero_usuarios_normal = int(input("Ingrese la cantidad de usuarios normales: \n"))
numero_usuarios_premium = int(input("Ingrese la cantidad de usuarios premium: \n"))
gastos_totales = float(input("Ingrese cantidad de gastos totales en CLP: \n"))

#Paso2 : Se realiza calculo
utilidad_usuarios_normal = precio_suscripcion * numero_usuarios_normal
utilidad_usuarios_premium = (1.5 * precio_suscripcion * numero_usuarios_premium)

utilidades = (utilidad_usuarios_normal + utilidad_usuarios_premium) - gastos_totales 

#Paso3 : Print de datos
print(f"Las utilidades del proyecto son: ${utilidades}.-")

