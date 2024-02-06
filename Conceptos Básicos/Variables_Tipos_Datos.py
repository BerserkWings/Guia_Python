"""
Estos son algunos ejemplos sobre variables y tipos de datos que se pueden utilizar en Python.
"""

print("\n-----------------------------------------------------------------------------------------------------------\n")
# Variable tipo String
print("\t Variable Tipo String \t\n")
cadena = "Esta es una cadena/string"

print("La variable cadena es del tipo: " + str(type(cadena)))

print(cadena)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Variable tipo Integer (Entero) y aplicando type casting
print("\t Variable Tipo Integer \t\n")
puertos = 65535

print("La variable puertos es del tipo: " + str(type(puertos)))

print("Actualmente existen estos puertos: " + str(puertos))  # str() para cambiar un dato a tipo string

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Variable tipo Float
print("\t Variable Tipo Float \t\n")
dinero = 155.89

print("La variable dinero es del tipo: " + str(type(dinero)))

print("\nTengo en mi cuenta: " + str(dinero) + " pesos. Estoy quebrado Unu")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Variable tipo booleano
print("\t Variable Tipo Booleano \t\n")

print("True es un valor tipo: " + str(type(True)))
print("False es un valor tipo: " + str(type(False)))

print("\n¿Es 1 igual a 1?: " + str(1 == 1))

print("¿Es 5 igual a 2?: " + str(5 == 2))


"""
Tipos de Type Casting:
str() -> Para convertir cualquier dato a tipo string

int() -> Para convertir cualquier dato a tipo int

float() -> Para convertir cualquier dato a tipo float
"""
