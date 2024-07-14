# distancia_ciudades.py

from geopy.distance import great_circle

# Datos ficticios para el ejemplo
ciudades = {
    "Santiago": (-33.4489, -70.6693),
    "Buenos Aires": (-34.6037, -58.3816),
    # Añadir más ciudades si es necesario
}

def calcular_distancia(ciudad_origen, ciudad_destino):
    coords_origen = ciudades.get(ciudad_origen)
    coords_destino = ciudades.get(ciudad_destino)

    if coords_origen and coords_destino:
        distancia = great_circle(coords_origen, coords_destino).km
        distancia_millas = distancia * 0.621371
        return distancia, distancia_millas
    else:
        return None, None

def main():
    print("Bienvenido al sistema de cálculo de distancia.")
    ciudad_origen = input("Ciudad de Origen: ")
    ciudad_destino = input("Ciudad de Destino: ")

    distancia_km, distancia_millas = calcular_distancia(ciudad_origen, ciudad_destino)

    if distancia_km is not None:
        print(f"La distancia entre {ciudad_origen} y {ciudad_destino} es de {distancia_km:.2f} km ({distancia_millas:.2f} millas).")
        print("Narrativa del viaje: La distancia entre las dos ciudades es de X km, lo que representa un viaje interesante.")
    else:
        print("Una o ambas ciudades no están en nuestra base de datos.")
    
    medio_transporte = input("Elige el medio de transporte (Auto/Avión): ")
    print(f"Medio de transporte elegido: {medio_transporte}")

    salida = input("¿Quieres salir? (s para salir): ")
    if salida.lower() == 's':
        print("Saliendo...")

if __name__ == "__main__":
    main()
