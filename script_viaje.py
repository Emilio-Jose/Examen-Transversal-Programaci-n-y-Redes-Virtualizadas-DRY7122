import requests

api_key = "db899651-cb31-452c-9212-98f77f259e6d"

print("Calculadora de distancia Chile - Argentina")

while True:
    origen = input("Ciudad de origen (s para salir): ")
    if origen == "s":
        break

    destino = input("Ciudad de destino: ")

    print("Medio de transporte")
    print("1 - Auto")
    print("2 - Bicicleta")
    opcion = input("Opción: ")

    if opcion == "1":
        vehiculo = "car"
        nombre = "auto"
    elif opcion == "2":
        vehiculo = "bike"
        nombre = "bicicleta"
    else:
        print("Opción inválida")
        continue

    # --- OBTENER COORDENADAS ORIGEN ---
    geo_url = "https://graphhopper.com/api/1/geocode"
    geo_origen = requests.get(geo_url, params={
        "q": origen + ", Chile",
        "key": api_key
    }).json()

    geo_destino = requests.get(geo_url, params={
        "q": destino + ", Argentina",
        "key": api_key
    }).json()

    lat_o = geo_origen["hits"][0]["point"]["lat"]
    lon_o = geo_origen["hits"][0]["point"]["lng"]
    lat_d = geo_destino["hits"][0]["point"]["lat"]
    lon_d = geo_destino["hits"][0]["point"]["lng"]

    # --- CALCULAR RUTA ---
    route_url = "https://graphhopper.com/api/1/route"
    ruta = requests.get(route_url, params={
        "point": [f"{lat_o},{lon_o}", f"{lat_d},{lon_d}"],
        "vehicle": vehiculo,
        "key": api_key
    }).json()

    km = ruta["paths"][0]["distance"] / 1000
    millas = km * 0.621371
    horas = ruta["paths"][0]["time"] / 3600

    print("\nResultado del viaje")
    print("Distancia km:", round(km, 2))
    print("Distancia millas:", round(millas, 2))
    print("Duración estimada:", round(horas, 2), "horas")
    print("Viaje en", nombre, "\n")

