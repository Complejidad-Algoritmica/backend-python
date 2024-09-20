# src/routes/generateDataset.py
import csv

def crear_grafo():
    grafo = {}

    # Cargar aeropuertos
    with open('airports.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Omitir el encabezado
        for row in reader:
            iata_code = row[4]  # Columna IATA
            if iata_code:
                grafo[iata_code] = []  # Inicializa el nodo

    # Cargar rutas
    with open('routes.csv', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Omitir el encabezado
        for row in reader:
            source = row[2]  # Aeropuerto de origen
            destination = row[4]  # Aeropuerto de destino
            if source in grafo and destination in grafo:
                grafo[source].append(destination)  # Añadir arista
                # Si las rutas son bidireccionales, descomentar la siguiente línea
                # grafo[destination].append(source)  # Añadir arista inversa

    return grafo

# Inicializa el grafo
grafo = crear_grafo()
