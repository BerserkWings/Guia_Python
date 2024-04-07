"""
Este es un ejemplo de práctica sobre lo visto en la estructura de datos
"""

# Creando lista de videojuegos
juegos = ["Cyberpunk 2077", "Fallout", "Starfield", "League of Legends"]

tope = 500

# Generos de videojuegos (diccionario)
generos = {
    "Cyberpunk 2077": "Rol",  # Juego: tipo_de_juego
    "Fallout": "Rol",
    "Starfield": "Aventura",
    "League of Legends": "MOBA"
}

# Ventas de videojuegos y Stock (diccionario)
ventas_stock = {
    "Cyberpunk 2077": (400, 200),  # Juego: (vendidos, en_stock)
    "Fallout": (600, 20),
    "Starfield": (300, 120),
    "League of Legends": (900, 360)
}

# Clientes (diccionario con conjunto)
clientes = {
    "Cyberpunk 2077": {"Yo", "Pepillo", "Tiji", "Lammer"},  # Juego: {dueños}
    "Fallout": {"Prit", "Yo", "Lammer", "Alex"},
    "Starfield": {"Tiji", "Pepillo", "Tomas", "Albert"},
    "League of Legends": {"Alex", "Tomas", "Yo", "Lammer"}
}


# Función que obtiene los datos de los diccionarios
def sumario(juego):
    print(f"\t[i] Resumen del juego {juego}")  # Obtiene mi juego favorito
    print(f"[+] Género del juego: {generos[juego]}")  # Obtiene el genero de mi juego favorito
    print(f"[+] Total de ventas para este juego: {ventas_stock[juego][0]}")  # Obtiene el ventas de ventas_stock
    print(f"[+] Total de stock de este juego: {ventas_stock[juego][1]}")  # Obtiene stock de ventas_stock
    print(f"[--] Clientes que han adquirido este juego: {', '.join(clientes[juego])}\n")  # Obtiene los clientes del juego


# Para juego en juegos, si en ventas_stock(vendidos) es mayor a tope, ejecuta función
for juego in juegos:
    if ventas_stock[juego][0] > tope:
        sumario(juego)


# Variable con lambda que calcula el total de ventas de los juegos cuyas ventas superan el límite tope.
ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_stock.items() if ventas_stock[juego][0] > tope)

print(f"[>] El total de ventas de todos los productos ha sido de: {ventas_totales()} productos.")
