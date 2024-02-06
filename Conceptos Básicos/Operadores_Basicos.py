"""
Estos son algunos ejemplos sobre los operadores básicos que se pueden utilizar en Python.
"""

# Declarando variables
numero1 = 10
numero2 = 15

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Operación Suma
print("\t Operación Suma \t\n")
print(numero1 + numero2)

print(f"Esto es una suma entre el número {numero1} y el número {numero2}, resultando en: " + str(numero1 + numero2))

resultado_suma = numero1 + numero2
print("Este es el resultado de la suma: " + str(resultado_suma))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Operación Resta
print("\t Operación Resta \t\n")
print(numero2 - numero1)

print(f"Esto es una resta entre el número {numero2} y el número {numero1}, resultando en: " + str(numero2 - numero1))

resultado_resta = numero2 - numero1
print("Este es el resultado de la resta: " + str(resultado_resta))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Operación Multiplicación
print("\t Operación Multiplicación \t\n")
print(numero1 * numero2)

print(f"Esto es una multiplicación entre el número {numero1} y el número {numero2}, resultando en: " + str(numero1 * numero2))

resultado_multiplicacion = numero1 * numero2
print("Este es el resultado de la multiplicación: " + str(resultado_multiplicacion))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Operación División
print("\t Operación División \t\n")
print(numero2 / numero1)

print(f"Esto es una división entre el número {numero2} y el número {numero1}, resultando en: " + str(numero2 / numero1))

resultado_division = numero2 / numero1
print("Este es el resultado de la división: " + str(resultado_division))

# Operación División con Función divmod()
print("\n\t Operación División con Función divmod() \t\n")
print(divmod(numero2, numero1))

print(f"Esto es una división entre el número {numero2} y el número {numero1}, usando la función divmod() nos devolvera "
      f"el cociente y el resto: " + str(divmod(numero2, numero1)))

resultado_division = divmod(numero2, numero1)
print("Este es el cociente y el resto resultante de la división: " + str(resultado_division))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Operación Cociente
print("\t Operación Cociente \t\n")
print(numero2 // numero1)

print(f"Esto es el cociente de una división, usando el número {numero2} como dividendo y el número {numero1} como "
      f"divisor resultando en: " + str(numero2 // numero1))

resultado_residuo = numero2 // numero1
print("Este es el cociente resultante de una división: " + str(resultado_residuo))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Operación Residuo
print("\t Operación Residuo \t\n")
print(numero2 % numero1)

print(f"Esto es el residuo de una división, usando el número {numero2} como dividendo y el número {numero1} como "
      f"divisor resultando en: " + str(numero2 % numero1))

resultado_residuo = numero2 % numero1
print("Este es el residuo resultante de una división: " + str(resultado_residuo))

print("\n-----------------------------------------------------------------------------------------------------------\n")

# Operación Potencias
print("\t Operación Potencias \t\n")
print(numero2 ** numero1)

print(f"Esto es el resultado de una potencia, usando el número {numero2} como base y el número {numero1} como "
      f"potencia, resultando en: " + str(numero2 ** numero1))

resultado_exponente = numero2 ** numero1
print("Este es el resultado de la potencia: " + str(resultado_exponente))

# Operación Potencias con Función Pow()
print("\n\t Operación Potencias con Función Pow()\t\n")
print(pow(numero2, numero1))

print(f"Esto es el resultado de una potencia, usando el número {numero2} como base y el número {numero1} como "
      f"potencia, resultando en: " + str(pow(numero2, numero1)))

resultado_pow = pow(numero2, numero1)
print("Este es el resultado de la potencia: " + str(resultado_pow))

print("\n-----------------------------------------------------------------------------------------------------------\n")

