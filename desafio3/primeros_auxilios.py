#Se imprime mensaje de bienvenida y se le pide a usuario ingresar opción Yes or No para iniciar programa
print("BIENVENIDO AL PROGRAMA DE PRIMEROS AUXILIOS")
estimulo = input("¿Responde a estimulos? [y/n]: ").lower()

#Se comienza a validar opciones ingresadas vs lo solicitado
if estimulo == "y":
    print("Valorar la necesidad de llevarlo al hospital más cercano")
else:
    print("Abrir la via Aérea")

    respira = input("¿Respira? [y/n]: ").lower()

    if respira == "y":
        print("Permitirle posición de suficiente ventilación")
    else:
        print("Administrar 5 ventilaciones y llamar a ambulancia")

        ambulancia= "n"
        while ambulancia == "n":
            signos_de_vida = input("¿Tiene signos de vida? [y/n]: ").lower()

            if signos_de_vida == "y":
                print("Reevaluar a la espera de la ambulancia")
            else:
                print("Administrar compresiones torácicas hasta que llegue la ambulancia")

            ambulancia=input("¿Llegó la ambulancia? [y/n]: ").lower()


print("Fin del programa")