"""
Estos son algunos ejemplos de la condicional if que entran en lo que es el control de flujo en Python.
"""

# Declarando variables
edad = 18
nueva_edad = 22
nacionalidad = "mexicana"
arma = "balas"

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional IF básica
print("\t Condicional if - Básica\t\n")

if edad <= 18:
    print("Eres mayor de edad")
else:
    print("Eres un mocoso")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional if - usando elif
print("\t Condicional if - Utilizando elif\t\n")

if edad < 13:
    print("Eres un mocoso")
elif 13 <= edad < 18:
    print("Eres un adolescente")
else:
    print("Ya eres un adulto, pagale al SAT")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional if - usando operador ternario
print("\t Condicional if - Operador Ternario\t\n")

mensaje = "Eres mayor de edad" if nueva_edad >= 18 else "Eres un mocoso"
print(mensaje)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional if - usando el operador lógico and
print("\t Condicional if - Operador Lógico AND\t\n")

if nueva_edad >= 18 and nacionalidad == "mexicana":
    print("Puedes votar en las selecciones mexicanas")
else:
    print("No eres mexa, zumbale alv")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional if - usando el operador lógico or
print("\t Condicional if - Operador Lógico OR\t\n")

if nueva_edad >= 18 or nacionalidad == "mexicana":
    print("Puedes votar en las selecciones mexicanas")
else:
    print("No eres mexa, zumbale alv")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional if - usando el operador lógico not
print("\t Condicional if - Operador Lógico NOT\t\n")

if not nacionalidad == "mexicana":
    print("No eres mexa, zumbale alv")
else:
    print("Bienvenido a la tierra de los dioses")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional if - usando operador especial in
print("\t Condicional if - Operador Especial IN\t\n")

if "mexicana" in nacionalidad:
    print("Bienvenido a la tierra de los dioses")
else:
    print("Saquese alv, no puedes entrar")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional if - usando operador especial not in
print("\t Condicional if - Operador Especial NOT IN\t\n")

if "balas" not in arma:
    print("Valimos cheto")
else:
    print("Te va a cargar el payaso")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional if - usando operador especial is
print("\t Condicional if - Operador Especial IS\t\n")

if 18 is 18:
    print("El número escrito es el mismo")
else:
    print("El número escrito NO es el mismo")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional if - usando operador especial is not
print("\t Condicional if - Operador Especial IS NOT\t\n")

if 18 is not 19:
    print("El número escrito NO es el mismo")
else:
    print("El número escrito es el mismo")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Condicional if en un bucle for
print("\t Condicional if en un Bucle For IS\t\n")

for i in range(10):
    if i == 5:
        print(f"Actualmente 'i' vale 5 [{i}]")
    else:
        print(f"Actualmente 'i' NO vale 5 [{i}]")

print("\n-----------------------------------------------------------------------------------------------------------\n")
