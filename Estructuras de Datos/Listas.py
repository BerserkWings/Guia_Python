"""
Estos son unos ejemplos de uso de las listas en Python.
"""

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando una lista y viendo su contenido
print("\t Listas - Creando una lista \t\n")

puertos_tcp = [21, 22, 25, 80, 443, 8080, 445, 69]

print("Imprimiendo lista: " + str(puertos_tcp) + "\n")

print("Imprimiendo cada elemento de la lista: ")
for puerto in puertos_tcp:
    print(f"Este es el puerto {puerto}")

puertos_tcp.sort()  # Ordenando puertos con sort()
print("\nPuertos ordenados: " + str(puertos_tcp))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Agregando y eliminando un elemento a la lista
print("\t Listas - Agregando/eliminando un elemento a la lista con append() y remove() \t\n")

cve_list = ['CVE-2023-1435', 'CVE-2022-45761', 'CVE-2023-7863']
print("Antes:\n" + str(cve_list))

cve_list.append('CVE-2021-43892')  # Agregando un elemento a la lista

cve_list.remove('CVE-2023-1435')  # Eliminando un elemento de la lista

print("\nDespués:\n" + str(cve_list))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Imprimiendo elementos deseados,  creando sublistas e invirtiendo posiciones de elementos
print("\t Listas - Imprimiendo elementos deseados, creando sublistas y invirtiendo posiciones de elementos \t\n")

attacks = ['Phishing', 'DDoS', 'SQL Injection', 'Man In The Middle', 'Cross-Site Scripting']
print("Lista normal: " + str(attacks))

# Indices de lista: [0, 1, 2, 3, 4]

# Imprimiendo elementos elegidos de la lista
primer_ataque = attacks[0]
cuarto_ataque = attacks[4]
print("\nImprimiendo ataques elegidos: " + str(primer_ataque) + ", " + str(cuarto_ataque))

# Creando sublistas - [1, 2, 3, 4, 5]
sublista1 = attacks[:3]
sublista2 = attacks[1:2]
sublista3 = attacks[:-3]
sublista4 = attacks[2:5]

print("\nImprimiendo sublistas: \n" + str(sublista1) + "\n" + str(sublista2) + "\n" + str(sublista3) +
      "\n" + str(sublista4))

# Invirtiendo lista
attacks.reverse()
print("\nLista inversa: " + str(attacks))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Imprimiendo lista con while, recorriendo lista con for y cambiando elementos a mayusculas y minusculas
print("\t Listas - Imprimiendo elementos de lista con while, recorriendo lista con for y cambiando elementos a "
      "mayusculas/minusculas \t\n")

# Usaremos la misma lista del ejemplo anterior
attacks2 = ['Phishing', 'DDoS', 'SQL Injection', 'Man In The Middle', 'Cross-Site Scripting']

# Imprimiendo lista con while
i = 0

print("Imprimeindo lista con while: ")
while i < len(attacks2):
    print(attacks2[i])
    i += 1

# Recorriendo una lista con for
s = 0
print("\nRecorriendo la lista con for: ")
for s, attacks2 in enumerate(attacks2):
    print(f"Para la posición {s+1} tendriamos el ataque {attacks2}")

# Imprimiendo lista en mayusculas
print("\nImprimiendo lista en mayusculas: ")
attacks_uppercase = [attack.upper() for attack in attacks]
print(attacks_uppercase)

print("\nImprimiendo lista en minusculas: ")
attacks_uppercase = [attack.lower() for attack in attacks]
print(attacks_uppercase)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Combinando elementos de lista y cambiando valor de un indice
print("\t Listas - Combinando elementos de lista y cambiando valor de un indice \t\n")

names = ["Luiz", "Piña", "Ale", "Yo"]
edades = [54, 32, 65, 49]

# Combinando listas
print("Imprimiendo listas combinadas: ")
for name, edad in zip(names, edades):
    print(f"{name} tiene {edad} años")

# Cambiando valor de un indice
print("\nCambiando valor de cualquier indice: ")
names[1] = "Chema Alonso"
names[3] = "El waos"

print(names)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Formas de eliminar elementos, formas de agregar elementos y limpiar lista
print("\t Listas - Formas de eliminar elementos, formas de agregar elementos y limpiando lista \t\n")

print("Lista normal: " + str(names))

# Formas de eliminar elementos
del names[1]  # Forma 1
names.remove("El waos")  # Forma 2
print("\nLista con elementos eliminados: " + str(names))

# Formas de agregar elementos
# Insertando elemento con insert(indice, elemento)
names.insert(1, "Chema Alonso")
print("\nInsertando un elemento: " + str(names))

# Insertando una lista en otra lista
more_names = ["Pepito", "Manolito"]
names.extend(more_names)
print("\nInsertando lista en otra lista: " + str(names))

# Eliminando último elemento con pop()
names.pop()
print("\nEliminando último elemento de lista: " + str(names))

# Limpiando lista con clear()
names.clear()
print("\nLimpiando lista: " + str(names))

print("\n-----------------------------------------------------------------------------------------------------------\n")
