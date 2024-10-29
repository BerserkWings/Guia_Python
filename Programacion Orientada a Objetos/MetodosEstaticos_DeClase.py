"""
Estos son algunos ejemplos de como se usan los metodos estaticos y algunos metodos de clase
"""

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Metodos Estaticos - Creando una clase con metodos estaticos \t\n")


# Creando una clase
class Calculadora:

    @staticmethod  # Creando un metodo estatico
    def suma(num1, num2):
        return num1 + num2

    @staticmethod
    def resta(num1, num2):
        return num1 - num2

    @staticmethod
    def multiplicacion(num1, num2):
        return num1 * num2

    @staticmethod
    def division(num1, num2):
        return num1 / num2 if num2 != 0 else "\n[!] Error: No se puede dividir un número entre cero\n"


# Utilizando metodos estaticos
print(Calculadora.suma(2, 8))
print(Calculadora.resta(10, 5))
print(Calculadora.multiplicacion(2, 5))
print(Calculadora.division(10, 2))
print(Calculadora.division(5, 0))

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Metodos de una Clase - Creando una clase con sus propios metodos \t\n")


# Creando una clase
class Automovil:
    def __init__(self, marca, modelo):  # Creando constructor
        self.marca = marca  # Creando atributos
        self.modelo = modelo

    @classmethod  # Creando metodo de clase
    def deportivos(cls, marca):  # 
        return cls(marca, "Sean")

    @classmethod  # Creando otro metodo de clase
    def sean(cls, marca):
        return cls(marca, "Deportivo")

    # Usando metodo str para obtener datos de las otras clases
    def __str__(self):
        return f"La marca {self.marca} es un modelo {self.modelo}"

# Creando e imprimiendo objetos
sean = print(Automovil.sean("Toyota"))
deportivo = print(Automovil.deportivos("Ferrari"))

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Combinando Metodos Estaticos y Metodos de Clase \t\n")


# Creando una clase
class Estudiantes:
    estudiantes = []

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        Estudiantes.estudiantes.append(self)

    @staticmethod
    def es_mayor_edad(edad):
        return edad >= 18

    @classmethod
    def crear_estudiantes(cls, nombre, edad):
        if cls.es_mayor_edad(edad):
            return cls(nombre, edad)
        else:
            print(f"\n[!] Error: El estudiante {nombre} es menor de edad. \n")

    @staticmethod
    def mostrar_estudiantes():
        for i, estudiantes in enumerate(Estudiantes.estudiantes):
            print(f"\n[+] Estudiante número[{i+1}]: {estudiantes.nombre}")


Estudiantes.crear_estudiantes("BerserkP", 457)
Estudiantes.crear_estudiantes("Pepin", 47)
Estudiantes.crear_estudiantes("Lupin", 32)
Estudiantes.crear_estudiantes("Papus", 31)

print("\n[i] Listando los estudiantes existentes:")
Estudiantes.mostrar_estudiantes()

print("\n-----------------------------------------------------------------------------------------------------------\n")
