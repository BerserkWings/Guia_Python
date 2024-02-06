"""
Las variables en Python son como nombres que se le asignan a los datos que manejamos. Piensa en una variable como un
nombre que pones a un valor, para poder referirte a él y utilizarlo en diferentes partes de tu código.

Variables
Una variable en Python es como un nombre que se le asigna a un dato. No es necesario declarar el tipo de dato, ya que
Python puede inferirlo.

Cadenas (Strings)
Las cadenas son secuencias de caracteres que se utilizan para manejar texto. Son inmutables, lo que significa que una
vez creadas, no puedes cambiar sus caracteres individuales.

Números
Python maneja varios tipos numéricos, pero nos centramos principalmente en:
- Enteros (Integers): Números sin parte decimal.
- Flotantes (Floats): Números que incluyen decimales.
"""

# Variable tipo String
cadena = "Esta es una cadena/string"

print(type(cadena))
print(cadena)

print()  # Este es un espacio namas

# Variable tipo Int (Entero) y aplicando type casting
puertos = 65535

print(type(puertos))
print("Actualmente existen estos puertos: " + str(puertos))  # str() para cambiar un dato a tipo string

print()

# Variable tipo Float
dinero = 155.89

print(type(dinero))
print("Tengo en mi cuenta: " + str(dinero) + " pesos. Estoy quebrado Unu")


"""
Tipos de Type Casting:
str() -> Para convertir cualquier dato a tipo string

int() -> Para convertir cualquier dato a tipo int

float() -> Para convertir cualquier dato a tipo float
"""
