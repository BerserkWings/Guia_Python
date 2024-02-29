"""
Estos son algunos ejemplos de uso de los diccionarios en Python
"""

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando un diccionario -> {clave: valor}
print("\t Diccionarios - Creando un diccionario \t\n")

# Diccionario global, usado en varios ejemplos
diccionario = {"nombre": "berserkp", "edad": 4345, "isla": "Ombligo de la luna"}

print("Este es mi diccionario: " + str(diccionario))

print(diccionario["nombre"])  # Imprimiendo el valor de un elemento del diccionario

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Modificando el valor de un elemento del diccionario
print("\t Diccionarios - Modificando el valor de una clave del diccionario \t\n")

diccionario["nombre"] = "papuBerserk"  # Cambiando el valor de la clave nombre

print("Cambiando el valor de clave 'nombre' a: " + diccionario["nombre"])

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Agregando un nuevo elemento al diccionario
print("\t Diccionarios - Agregando un nuevo elemento al diccionario \t\n")

diccionario["profesion"] = "hacker"  # Agregando un elemento nuevo al diccionario

print("El nuevo diccionario: " + str(diccionario))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Eliminando elementos de diccionario
print("\t Diccionarios - Eliminando elementos de diccionarios \t\n")

del diccionario["edad"]  # Eliminando un elemento del diccionario

print("Nuevo diccionario: " + str(diccionario))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Revisando si existe un elemento en el diccionario
print("\t Diccionarios - Buscando un elemento del diccionario \t\n")

if "nombre" in diccionario:
    print("Esta clave, existe en el diccionario")
else:
    print("Esta clave, NO existe en el diccionario")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Iterando en un diccionario para obtener la clave y el valor de todo el diccionario
print("\t Diccionarios - Iterando en el diccionario para obtener valores\t\n")

# Utilizando for para iterar
# Forma 1: Usando el metodo items()
for key, value in diccionario.items():
    print(f"Para la clave '{key}', tendremos el valor '{value}'")
    print(f"Representados en el diccionario: [{key}]: {value}\n")

# Forma 2: Usando el metodo keys() y values()
for clave in diccionario.keys():
    print("Clave: " + clave + "\n")

for valor in diccionario.values():
    print("Valor: " + valor + "\n")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Limpiando el diccionario
print("\t Diccionarios - Limpiando diccionario \t\n")

otro_diccionario = {"nombre": "berserkp", "edad": 4345, "interes": "Chambear"}

print(f"La longitud del diccionario es de {len(otro_diccionario)} elementos")
print(otro_diccionario)

# Limpiando diccionario con el metodo clear()
otro_diccionario.clear()

print(f"\nLa longitud del diccionario es de {len(otro_diccionario)} elementos")
print(otro_diccionario)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando diccionario de comprensión
print("\t Diccionarios - Creando diccionario de comprensión \t\n")

cuadrados = {x: x**2 for x in range(6)}  # Diccionario que se llena de cuadrados de X

print(cuadrados)
print(cuadrados.keys())
print(cuadrados.values())

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Obteniendo elemento del diccionario
print("\t Diccionarios - Obteniendo un elemento del diccionario \t\n")

print("Obteniendo valor de clave 'nombre': " + diccionario.get("nombre", "No encontrado"))  # Usando metodo get(clave a buscar, si no lo encuentra muestra un mensaje)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Actualizando diccionario + agregando otro diccionario al diccionario
print("\t Diccionarios - Actualizando / agregando otro diccionario al diccionario \t\n")

new_diccionario = {"nombre": "berserkp", "edad": 4345, "interes": "Chambear"}

diccionario.update(new_diccionario)  # Actualizando el diccionario, si los elementos se repiten, se ignoran

print("Nuevo diccionario: " + str(diccionario))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Diccionarios anidados
print("\t Diccionarios - Creando diccionario anidado \t\n")

mi_dict = {
    "nombre": "SuperBerserk",
    "hobbies": {"Primero": "Videojuegos", "Segundo": "Pajas"},
    "edad": 2943
}

print(mi_dict["nombre"])
print(mi_dict["hobbies"]["Segundo"])  # Imprimiendo el valor de un elemento del diccionario hobbies

print("\n-----------------------------------------------------------------------------------------------------------\n")
