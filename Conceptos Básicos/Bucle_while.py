"""
Estos son unos ejemplos sobre el bucle while en Python.
"""

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando un bucle while
print("\t Bucle While \t\n")

i = 0  # Contador

while i < 5:
    print(i)
    i += 1  # Incrementando i por 1

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Usando bucle while con condicional
print("\t Bucle While - Usando una condicional \t\n")

# Forma 1
p = 0
while p < 10:
    if p == 10:
        break
    p += 1
else:
    print("El bucle terminó normalmente \n")

# Forma 2
s = 0
while s < 16:
    if s == 10:
        print("Salimos antes de tiempo")
        break
    s += 1
else:
    print("El bucle terminó normalmente")

print("Estamos fuera del bucle")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Usando break y continuo en while
print("\t Bucle While - Rompiendo y continuando bucle \t\n")

# Usando break
contador = 0

while True:  # Bucle infinito
    print(contador)
    contador += 1
    if contador >= 5:
        break
print("Bucle terminado \n")

# Usando continue
contador2 = 0

while contador2 < 5:
    contador2 += 1
    if contador2 == 3:
        continue  # Pasar a la siguiente iteración sin imprimir si contador es igual a 3
    print(f"Continua el bucle {contador2}")
print("Fin del bucle")

print("\n-----------------------------------------------------------------------------------------------------------\n")
