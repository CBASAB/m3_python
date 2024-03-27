## DICCIONARIOS ##
"""
PAR -> {CLAVE:VALOR}
La clave debe ser UNICA -> Si existe duplicidad retorna solo la ultima referencia de valor


"""
# Diccionario vacio
notas = {}
# Creacion de un diccionario
notas = {
    "Camila": 7,
    "Antonio": 5,
    "Felipe": 6,
    "Antonia": 7,
    #"Antonia": 6 -> Si tengo una clave repetida, me va a traer el ultimo
    }

print(notas) # {'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Antonia': 7}

#Acceder a los valores del diccionario
print(notas["Camila"]) # 7
print(notas["Antonio"]) # 5
print(notas["Felipe"]) # 6
print(notas["Antonia"]) # 7
#print(notas["Mijail"]) # KeyError: 'Mijail'
#print(notas["Felip"]) # KeyError: 'Felip' -> Indica que no existe esa clave (minuscula tambien pasaria lo mismo porque la F esta en mayuscula)

# Agregar par clave:valor al diccionario
# diccionario[clave] = valor
notas["Mijail"]= 7
print(notas) # {'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Antonia': 7, 'Mijail': 7} -> Agrego en la ultima posicion
notas["Julio"]= 7
print(notas) # {'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Antonia': 7, 'Mijail': 7, 'Julio': 7}

# Cambiar el valor de una clave
notas["Felipe"]= 7
print(notas) # {'Camila': 7, 'Antonio': 5, 'Felipe': 7, 'Antonia': 7, 'Mijail': 7, 'Julio': 7}

# Eliminar elementos de un diccionario
# Con del
del notas["Antonia"]
print(notas) # {'Camila': 7, 'Antonio': 5, 'Felipe': 7, 'Mijail': 7, 'Julio': 7}

# Con pop -> Al eliminar permite capturar el elemento
eliminado = notas.pop("Antonio")
print(eliminado) # 5
print(notas) # {'Camila': 7, 'Felipe': 7, 'Mijail': 7, 'Julio': 7}

# Unir diccionarios .update

notas2 ={
    "Alexis" : 6,
    "Yasna" : 6,
    #"Camila" : 3 # Al volver a agregar la misma clave del diccionario1 (notas), lo reemplaza
}

notas.update(notas2) # {'Camila': 7, 'Felipe': 7, 'Mijail': 7, 'Julio': 7}
print(notas) # {'Camila': 7, 'Felipe': 7, 'Mijail': 7, 'Julio': 7, 'Alexis': 6, 'Yasna': 6}


