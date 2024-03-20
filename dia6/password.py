#Captura de datos
contrasenia = input("Ingrese una contraseña (Min 6 caracteres):\n")

#string.count("")
if contrasenia.count(" ") > 0:
    print("El password no puede contener espacios")
elif contrasenia == "12345":
    print("El password es incorrecto")
elif len(contrasenia) < 6:
    print("El password es demasiado corto")
else:
    print("El formato de password es correcto")

#Validar que si el usuario ingresa 12345 -> El password es incorrecto

"""else:
    #len -> Contar los caracteres que tenga el string
    if len(contrasenia) < 6:
        print("El password es demasiado corto")
"""
print("Programa terminado")