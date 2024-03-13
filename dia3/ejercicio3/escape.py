from math import sqrt

#paso 1: capturar los datos (string) y conversion
#radio = float(input("Ingrese el radio en kilometros")) * 1000

radio_kilometros = input("Ingrese el radio en kilometros")
radio_kilometros = float(radio_kilometros)
radio_metros = radio_kilometros * 1000

constante_gravitacional = input("Ingrese la constante de gravedad del planeta en [mt/s2]")
constante_gravitacional = float(constante_gravitacional)#conversion de string a float

#paso 2: Resolver fomula Ve = raiz_cuadrada(2* constante_gravitacional * radio_metros)
velocidad_escape = sqrt(2 * constante_gravitacional * radio_metros)

#paso 3: Mostrar resultado final
print(f"La velocidad de Escape es {round(velocidad_escape,1)} [m/s]")