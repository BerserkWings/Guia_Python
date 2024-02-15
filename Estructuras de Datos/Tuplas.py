"""
Estos son algunos ejemplos de como son las tuplas en Python.
"""

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando una tupla
print("\t Tuplas - Creando una lista \t\n")

example = (1, 2, 3, 4, 5, 6)
print(example)

# Imprimiendo los elementos de las tuplas usando rangos
print(example[1:3])
print(example[2:])
print(example[:3])

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Tupla con elementos variados
print("\t Tuplas - Almacenando distintos datos \t\n")

example2 = (1, "test", [1, 2, 3], 4, True, 5)

print("Imprimiendo los elementos de la tupla: ")
for element in example2:
    print(element)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Asignando elementos de una tupla a distintas variables
print("\t Tuplas - Asignando elementos de una tupla a distintas variables \t\n")

mi_tupla = (1, 2, 3, 4, 5)
a, b, c, d, e = mi_tupla

print(a)
print(b)
print(c)
print(d)
print(e)

print("\nImprimiendo variables: ", str(a), str(b), str(c), str(d), str(e))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Juntando elementos de varias tuplas
print("\t Tuplas - Juntando elementos entre tuplas \t\n")

primer_tupla = (1, 2, 3, 4)
segunda_tupla = (5, 6, 7, 8)

tercer_tupla = primer_tupla + segunda_tupla

print("Imprimiendo tuplas combinadas: \n" + str(tercer_tupla))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Repitiendo elementos de tuplas
print("\t Tuplas - Repitiendo los elementos de una tupla \t\n")

cuarta_tupla = primer_tupla*3  # Aquí es donde le damos la cantidad a repetir la tupla

print("Multiplicando por 3 la primer tupla: " + str(cuarta_tupla))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Identificando elementos de tupla y creando nueva tupla con la respuesta
print("\t Tuplas - Identificando los elementos de una tupla y el resultado sera otra tupla \t\n")

otra_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)

numeros_pares = tuple(i for i in otra_tupla if i % 2 == 0)  # La función tuple() transforma en tupla cualquier dato

print(numeros_pares)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Caso practico de que las tuplas no se pueden modificar
print("\t Tuplas - Caso práctico \t\n")

db1_credential = ("berserkp", "berserkp123")
db2_credential = ("luiz", "luiz123")

try:
    db1_credential[0] = "lamer"
except:
    print("No es posible manipular los elementos de una tupla")

print("\n-----------------------------------------------------------------------------------------------------------\n")

