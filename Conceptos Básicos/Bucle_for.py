"""
Estos son unos ejemplos de como usar el bucle for en Python
"""

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Uso Bucle for y función range(inicio, fin, por pasos)
print("\t Bucle For - función range() \t\n")

for i in range(5):
    print(i)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Uso del Bucle for con Condicional if
print("\t Bucle For con Condicional if \t\n")

for i in range(5):
    if i == 5:
        break
    else:
        print("Bucle concluido exitosamente")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Imprimiendo datos de una lista
print("\t Bucle For - Imprimiendo datos de una lista \t\n")

names = ["Papu", "Prro", "Hacker", "Lolsito"]

for name in names:
    print(f"El nombre para esta vuels es {name}")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Usando función enumerate en for para enumerar datos de lista
print("\t Bucle For - Función enumerate() \t\n")

for i, nombre in enumerate(names):
    print(f"Nombre [{i+1}]: {nombre}")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Iterando en un diccionario con el bucle for para obtener datos
print("\t Bucle For - Iterando en diccionario \t\n")

frutas = {"manzana": 1, "platanos": 5, "kiwis": 3}

for fruta, cantidad in frutas.items():
    print(f"Hay {cantidad} cantidades de la fruta {fruta}")
    print(f"Tengo {cantidad} {fruta}(s)")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Bucles anidados
print("\t Bucle For - Creando bucle anidado \t\n")

my_list = [[1, 4, 5], [2, 6, 8], [9, 4, 1]]

for element in my_list:
    print(f"\n[+] Vamos a desglosar la lista {element}\n")
    for element_in_list in element:
        print(element_in_list)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando una comprensión de lista usando for
print("\t Bucle For - Creando una comprensión de lista \t\n")

odd_list = [1, 3, 5, 7, 9]
cuadrado = [i ** 2 for i in odd_list]  # Comprensión de lista (for)

print(cuadrado)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Rompiendo y continuando bucles
print("\t Bucle For - Rompiendo y continuando bucles \t\n")

# Rompiendo bucle con condicional
for i in range(10):
    if i == 5:
        print(i)

# Utilizando break para romper bucle
for i in range(10):
    if i == 5:
        break
print("\n Se rompio bucle \n")

# Continuando el bucle
for i in range(10):
    if i == 5:
        continue
    print(i)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Ejercicio practico usando bucle for, condicionales, etc
print("\t Bucle For - Ejercicio práctico \t\n")

numbers = [2, 4, 6, 8, 10, 7, 12, 14]
todos_son_pares = True

for number in numbers:
    if number % 2 != 0:
        todos_son_pares = False
        break

if todos_son_pares:
    print("Todos los elementos de la lista son pares")
else:
    print("Alguno de los elementos de la lista es impar")

print("\n-----------------------------------------------------------------------------------------------------------\n")
