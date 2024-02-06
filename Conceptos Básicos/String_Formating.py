"""
Estos son unos ejemplos de como usar los posicionadores en Python.
"""

# Posicionadores
"""
%s -> Para strings
$d -> Para números enteros
$f -> Para números con decimales
"""

# Declarando Variables
name = "berserkp"
rol = "lammer"
edad = 1232
dinero = 155.89

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Probando Posicionador %s \t\n")
print("Hola, mi nombre es %s" % name)

print("Hola, mi nombre es %s y soy un %s" % (name, rol))

print("\n\t Probando Posicionador %d \t\n")

print("Hola, mi nombre es %s y soy un %s. Actualmente tengo %d años." % (name, rol, edad))

print("\n\t Probando Posicionador %f \t\n")

print("Hola, mi nombre es %s y soy un %s. Actualmente tengo %d años y en el banco tengo %f pesos, estoy quebrado Unu" %
      (name, rol, edad, dinero))

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Probando Función Format() \t\n")

print("Hola soy {}!".format(name))

print("Hola soy {}! y tengo {} años.".format(name, edad))

print("Hola soy {1}! y tengo {0} años. Estoy jugando jeje, soy {0} y tengo {1}".format(name, edad))  # Usando indices

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Probando F-Strings \t\n")

print(f"Hola, soy {name} y tengo {edad} años. Actualmene soy un {rol} y tengo {dinero} pesos en mi cartera.")

print("\n-----------------------------------------------------------------------------------------------------------\n")
