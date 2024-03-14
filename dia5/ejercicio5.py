edad = 27
#¿Juan es mayor de edad?
print (edad >= 18)#True
print (edad < 18)#False

edad_graduacion_colegio = 17
#¿Juan se graduo antes de los 18 años?
print(edad_graduacion_colegio < 18) #True
print(edad_graduacion_colegio >= 18) #False

experiencia_laboral = 4
#¿Juan NO tiene 4 años de experiencia laboral?
print( experiencia_laboral != 4) #False
print( experiencia_laboral == 4) #True

numero_hijos = 0
#¿Juan tien hijos? Tenemos varias formas de preguntar lo mismo
print (numero_hijos > 0) #False
print (numero_hijos == 0) #True
print (numero_hijos < 1) #True
print (numero_hijos != 0) #False
print (numero_hijos >= 1) #False 
# numero_hijos > 1 o numero_hijos = 1
# False       v        False = False



"""
    1.- Si las exportaciones disminuyen entonces bajarán las utilidades -> Si las utilidades suben, las exportaciones aumentan
    2.- Los precios son altos si y sólo sí los costos aumentan -> Si los costos aumentan, los precios aumentan
    3.- Si la producción aumenta entonces bajarán los precios -> 
    4.- Si la contaminación aumenta entonces existirá restricción vehicular adicional -> 
    
    5.- Ser o no ser
    6.- La programacion no es facil -> Es dificil la programacion
"""

nombre = "Juan"
me_llamo_juan = (nombre == "Juan")
print(me_llamo_juan) #True
print(type(me_llamo_juan)) #<class 'bool'>



#Logica proposicional
"""
# Quieres helado (P) SI - NO
# Quieres bebida (Q) SI - NO

# AND (Y; i) 2 ^ 2
# Quieres helado y Quieres bebida
# Punto critico para el AND es : ambos verdaderos el resultado es verdadero
    P            y      Q
-------
    True         y      True   = True (* Este es unico que debo aprender, porque si sabes este todo lo demas es False)
    True         y      False  = False
    False        y      True   = False
    False        y      False  = False

#Punto critico para el o es: ambos falsos el resultado es falso
    P            o      Q
-------
    True         o      True   = True
    True         o      False  = True
    False        o      True   = True
    False        o      False  = False (* Este es unico que debo aprender, porque si sabes este todo lo demas es True)

#Punto critico para el ^ (XoR) es: ambas iguales el resultado es False, si ambas son diferentes es True
    P            ^      Q
    
    
    
"""

