

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Clases - Creando una clase \t\n")


class Persona:  # Creando una clase
    def __init__(self, nombre, edad):  # Creando constructor y dandole atributos, ej. def __contructor_(atributos):
        self.nombre = nombre  # Creando atributos
        self.edad = edad

    def saludo(self):  # Creando un metodo, ej. def nombre_metodo(atributos metodo)
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"


# Creando objeto
berserkp = Persona("berserkp", 535)  # Usando clase, ej. nombre_clase(atributos_clase)

# Imprimiendo objeto
print(berserkp.saludo())  # Usando objeto y metodo de la clase

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Clases - Creando una Clase con 2 Objetos \t\n")


class animal:  # Creando una clase
    def __init__(self, nombre, animal):  # Creando constructor
        self.nombre = nombre  # Creando atributos
        self.animal = animal

    def descripcion(self):  # Creando metodo
        print(f"{self.nombre} es un {self.animal}")


# Creando objetos
gato = animal("Rivers", "Gato")  # Creando un objeto
perro = animal("Vixi", "Perro")

# Usando metodo de la clase en objetos
gato.descripcion()
perro.descripcion()

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Clases - Creando una Clase con 2 Metodos\t\n")


class CuentaBancaria:  # Creando Clase
    def __init__(self, cuenta, nombre, dinero=0):  # Creando constructor
        self.cuenta = cuenta  # Creando atributos
        self.nombre = nombre
        self.dinero = dinero

    def depositar_dinero(self, dinero):  # Creando metodo con atributo propio
        self.dinero += dinero  # Dinero introducido en clase más dinero introducido en metodo
        return (f"\n[++] [{self.nombre}] Se han depositado {dinero} euros, actualemente  el balance actual de la cuenta"
                f"es de {self.dinero} euros.")

    def retirar_dinero(self, dinero):
        if dinero > self.dinero:  # Si dinero introducido en metodo es mayor a dinero introducido en clase, entonces
            return f"\n[!] Operación denegada: Fondos Insuficientes"

        self.dinero -= dinero  # Dinero introducido en clase menos dinero introducido en metodo
        return (f"\n[++] [{self.nombre}] Se han retirado {dinero} euros, actualmente el  balance actual de la cuenta es de "
                f"{self.dinero} euros")


berserkp = CuentaBancaria("123456", "BerserkP", 1000)  # Creando objeto

print(berserkp.depositar_dinero(500))
print(berserkp.retirar_dinero(2000))
print(berserkp.depositar_dinero(250))

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Clases - Decorador Property y Metodos Especiales String y Eq\t\n")


class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

# Usando decorador @property para poder usar el atributo del metodo en modo lectura, útil cuando quieres calcular un
# valor basado en otros atributos de la clase sin que el usuario tenga que llamar explícitamente a un método para obtener ese valor.

    @property
    def area(self):
        return self.ancho * self.alto


# Usando metodo especial _str_, se utiliza para definir la representación de cadena de un objeto. Útil para una
# representación legible en cadena de un objeto, facilita la depuración y la comprensión del estado de un objeto cuando
# se imprime o se muestra en un contexto donde se espera una cadena.

    def _str_(self):
        return f"\n[+] Propiedades del rectangulo: [Ancho:{self.ancho}][Alto: {self.alto}]"


# Usando metodo especial _eq_, se utiliza para definir la comparación de igualdad entre dos objetos
    def _eq_(self, other):
        return self.ancho == other.ancho and self.alto == other.alto


rec1 = Rectangulo(20,80)
rec2 = Rectangulo(10,60)

print(rec1)
print(f"\n[++] El area es: {rec1.area}")
print(f"\n[?] ¿Son iguales? -> {rec1 == rec2}")

print("\n-----------------------------------------------------------------------------------------------------------\n")

print("\t Clases - Decorador staticmethod y classmethod\t\n")


class Libro:  # Creando clase

    IVA = 0.21

    def __init__(self, titulo, autor, precio):  # Creando constructor
        self.titulo = titulo # Creando atributos
        self.autor = autor
        self.precio = precio

# Se utiliza para definir un método estático dentro de una clase. Un método estático es un método que pertenece a la
# clase en sí misma, Esto significa que no requiere una instancia de la clase para ser invocado.
    @staticmethod
    def es_bestseller(self, total_ventas):
        return total_ventas > 5000

# Se utiliza para definir métodos de clase dentro de una clase. Un método de clase es un método que opera en la clase
# misma en lugar de en instancias individuales de la clase
    @classmethod
    def precio_con_iva(cls, precio):
        return precio + precio * cls.IVA


class LibroDigital(Libro):
    IVA = 0.10


# Creando objetos
mi_libro = Libro("¿Como ser un buen hacker?", "BerserkP", 17.5)
mi_libro_digital = LibroDigital("Iniciación al lammer", "BerserP", 17.5)

print(f"\n[++] El precio del libro con IVA incluido es de {Libro.precio_con_iva(mi_libro.precio)}")
print(f"\n[++] El precio del libro digital con IVA incluido es de {LibroDigital.precio_con_iva(mi_libro_digital.precio)}")

print("\n-----------------------------------------------------------------------------------------------------------\n")

