"""
Estos son algunos ejemplos de como usar y crear funciones en Python.
"""

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando una función
print("\t Función \t\n")

def saludo():
    print("Hola, esto es un saludo xd")

saludo()  # Llamando a la función para su ejecución

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando una función con argumentos
print("\t Función - Agregando argumentos \t\n")

def saludin(nombre):
    print(f"Hola {nombre}, esto es un saludin xd")

saludin("BerserkWings")

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Caso practico y utilizando return
print("\t Función - Usando return \t\n")

def suma(x, y):
    return x + y

print(f"La suma de ambos valores es: {suma(10, 15)}")


print("\n-----------------------------------------------------------------------------------------------------------\n")

# Ambito de las variables
print("\t Ambito de Variables - Creando una variable global \t\n")

variable_global = "Soy una variable global"

def mi_funcion():
    print(variable_global)

mi_funcion()
print(variable_global)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Imprimiendo el valor de una variable global que esta dentro de una función
print("\t Ambito de Variables - Imprimiendo una variable global dentro de una función \t\n")

new_variable = None
def otra_funcion():
    global new_variable  # Convirtiendo la variable new_variable en global
    new_variable = "Soy una nueva variable global"
    print(new_variable)

otra_funcion()
print(new_variable)  # Imprimiendo el valor de la variable global fuera de la función

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Modificando una variable global
print("\t Ambito de Variables - Modificando una variable global \t\n")

variable_global = "Soy una variable global"
print(variable_global)

def nueva_funcion():
    global variable_global
    variable_global = "sigo siendo global, pero me modificaron"
    print(variable_global)

nueva_funcion()
print(variable_global)  # Imprimiendo el valor de la variable global fuera de la función

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Creando una función lambda
print("\t Función lambda - Creando una función lambda \t\n")

funcion_lambda = lambda: "Hola mundo"

print(funcion_lambda)  # Mostrara la dirección de memoria de la función

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Agregando un argumento a una función lambda
print("\t Función lambda - Agregando un argumento a una función lambda \t\n")

cuadrado = lambda x: x**2  # lambda argumentos: operación
print(cuadrado(7))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Agregando más de un argumento
print("\t Función lambda - Agregando más de un argumento a una función lambda \t\n")

suma = lambda x, y: x+y

print(suma(9, 91))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Jugando con los elementos de una lista
print("\t Función lambda - Retornando una lista con el cuadrado de sus elementos \t\n")

numeros = [1, 2, 3, 4, 5, 6, 7, 8]

# Usamos función list() para convertir un iterable en una lista
cuadrados = list(map(lambda x: x**2, numeros))  # map() permite aplicar una función a todos los iterables

print(cuadrados)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Analizando elementos de una lista
print("\t Función lambda - Usando función filter() para encontrar los números pares \t\n")

pares = list(filter(lambda x: x % 2 == 0, numeros))  # Usamos la función filter() para filtrar elementos de un iterable usando una función de filtro

print(pares)

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Probando el modulo reduce
print("\t Función lambda - Usando modulo reduce() para multiplicar todos los elementos de una lista \t\n")

from functools import reduce  # Importamos la libreria functools para usar la función reduce()

otros_numeros = [1, 2, 3, 4, 5, 6, 7, 8]

producto = reduce(lambda x, y: x*y, otros_numeros)  # La función reduce() aplica repetidamente la función a los elementos iterables

print(producto)

print("\n-----------------------------------------------------------------------------------------------------------\n")
