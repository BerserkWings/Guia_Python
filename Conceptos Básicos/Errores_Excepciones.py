"""
Estos son algunos ejemplos de uso del try y except en Python
"""

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando una excepción
print("\t Errores y Excepciones - Creando una Excepción \t\n")

try:
    num = 5/0

except ZeroDivisionError:
    print("Error: No se puede dividir un número entre cero")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando una excepción que indica el error de un valor
print("\t Errores y Excepciones - Creando una Excepción tipo error en valor \t\n")

try:
    int("Hola mundo")
except ValueError:
    print("Error: Esto es un error de valor")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Indicando el tipo de error con una excepción
print("\t Errores y Excepciones - Indicando el tipo de error \t\n")

from pwn import log  # Importando libreria para poner chulo el mensaje de error

try:
    num = "hola" / 0
except ZeroDivisionError:
    print("No se puede dividir un número entre cero")
except TypeError:  # Esta excepción hace que se muestre el error en la terminal
    log.failure("Las operatorias matematicas solo se hacen con números")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Usando else y finally
print("\t Errores y Excepciones - Usando else y finally \t\n")

num = 1

try:
    num / 0

except ZeroDivisionError:
    print("No se puede dividir un número entre cero")
except TypeError:  # Esta excepción hace que se muestre el error en la terminal
    log.failure("Las operatorias matematicas solo se hacen con números")
else:
    print(f"La división de ambos números da como resultado: {num}")
finally:  # Lo que este dentro del finally siempre se va a ejecutar
    print("Esto siempre se va a ejecutar")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Generando una excepción manual con raise
print("\t Errores y Excepciones - Generando una excepción manual \t\n")

x = -5

if x < 0:
    raise Exception("No se pueden utilizar números negativos")

print("\n-----------------------------------------------------------------------------------------------------------\n")
