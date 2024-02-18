"""
Estos son algunos ejemplos de uso de los conjuntos en Python
"""

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando un conjunto
print("\t Conjuntos - Creando un conjunto \t\n")

mi_conjunto = {1, 2, 3}

print(mi_conjunto)
print(type(mi_conjunto))  # Un conjunto devuelve un valor llamado set

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Añadiendo algunos elementos al conjunto
print("\t Conjuntos - Añadiendo elementos a un conjunto \t\n")

otro_conjunto = {1, 2, 3, 4, 5}

otro_conjunto.add(6)  # Añadiendo otro elemento al conjunto
otro_conjunto.add(7)  # No siempre estaran ordenados los elementos

print(otro_conjunto)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Incorporando un conjunto a otro conjunto
print("\t Conjuntos - Incorporando conjuntos entre si \t\n")

conjunto = {1, 2, 3}

conjunto.update({4, 5, 6})

print(conjunto)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Eliminando elementos de un conjunto
print("\t Conjuntos - Eliminando elementos de un conjunto \t\n")

prueba = {1, 2, 3, 4, 5}

prueba.discard(3)  # Eliminando un elemento

print(prueba)

prueba.discard(5)

print(prueba)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Intersección de conjuntos (mostrando los elementos repetidos en 2 conjuntos)
print("\t Conjuntos - Mostrando elementos repetidos en 2 conjuntos \t\n")

prueba1 = {1, 2, 3, 4, 5}
prueba2 = {3, 4, 5, 6, 6}

conjunto_final = prueba1.intersection(prueba2)  # Encontrando elementos repetidos

print("Elementos repetidos: " + str(conjunto_final))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando union de conjuntos, esto quita las repeticiones
print("\t Conjuntos - Union de conjuntos \t\n")

conjunto1 = {1, 2, 3}
conjunto2 = {1, 2, 3, 4, 5, 6}

conjunto3 = conjunto1.union(conjunto2)  # Uniendo conjuntos. OJO, no siempre estaran ordenados

print(conjunto3)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Verificando si un conjunto es un subconjunto de un conjunto, si es correcto da True
print("\t Conjuntos - Subconjunto de un conjunto \t\n")

# Utilizamos los conjuntos del ejercicio anterior
print(conjunto1.issubset(conjunto2))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Convirtiendo lista en un conjunto y luego a lista otra vez
print("\t Conjuntos - Convirtiendo lista en conjunto y viceversa \t\n")

mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

no_repeat = set(mi_lista)  # Convirtiendo la lista en un conjunto

print(no_repeat)

no_repeat = list(set(mi_lista))  # Convirtiendo conjunto en lista

print(no_repeat)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Script para hacer busquedas rapidas de un número existente en un conjunto
print("\t Conjuntos - Buscando un elemento dentro de un conjunto \t\n")

super_conjunto = set(range(10000))  # Conjunto de 10k elementos

print(899 in super_conjunto)  # Buscando el elemento. Si existe el número en el conjunto, da un True, si no, da un False

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Ejemplo práctico
print("\t Conjuntos - Ejercicio práctico \t\n")

usuarios_face = {"Luiz", "Piña", "Ale", "Yo"}
usuarios_X = {"Luiz", "Yo", "Piña", "Pepito", "Manolo"}

ambas_plataformas = usuarios_face.intersection(usuarios_X)  # Mostrando usuarios iguales registrados en ambas plataformas

print("Estos son los usuarios que estan en ambas plataformas: " + str(ambas_plataformas))

todos_los_usuarios = usuarios_face.union(usuarios_X)  # Mostrando todos los usuarios
print("Mostrando todos los usuarios: " + str(todos_los_usuarios))

diferencias_entre_plataformas = usuarios_face.difference(usuarios_X)  # Mostrando usuarios que no estan en alguna plataforma

print("Mostrando que usuario no se encuentra en X: " + str(diferencias_entre_plataformas))

print("\n-----------------------------------------------------------------------------------------------------------\n")
