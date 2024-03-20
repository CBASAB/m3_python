estimulo = input("BIENVENIDO AL PROGRAMA DE PRIMEROS AUXILIOS \n ¿Responde a estimulos? [y/n]: ").lower()

if estimulo == "y":
    print("Valorar la necesidad de llevarlo al hospital mas cercano")
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

            ambulancia=input("¿Llego la ambulancia? [y/n]: ").lower()


print("Fin del programa")