# src/routes/generateDataset.py
import csv, os, random

def crear_grafo():
    grafo = {}

    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, '../datasets/airports.csv')

    # Cargar aeropuertos
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # Omitir el encabezado
        for row in reader:
            if row[0] == '100': break
            iata_code = row[4]  # Columna IATA
            if iata_code:
                grafo[iata_code] = []  # Inicializa el nodo
    
    file_path = os.path.join(current_directory, '../datasets/routes.csv')

    # Cargar rutas
    with open(file_path, newline='', encoding='utf-8') as f:
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

def descargar_grafo(grafo: dict) -> dict:
    # generate a .txt file with the graph
    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, "../img/graph.txt")
    with open(file_path, "w") as f:
        for k, v in grafo.items():
            f.write(f"{k}: {v}\n")


def crear_grafo_con_destinos() -> dict:
    graph = dict()

    current_directory = os.path.dirname(__file__)
    file_path = os.path.join(current_directory, '../datasets/airports.csv')

    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        """        
        Airport ID	Unique OpenFlights identifier for this airport.
        Name	Name of airport. May or may not contain the City name.
        City	Main city served by airport. May be spelled differently from Name.
        Country	Country or territory where airport is located. See Countries to cross-reference to ISO 3166-1 codes.
        IATA	3-letter IATA code. Null if not assigned/unknown.
        ICAO	4-letter ICAO code.
        Null if not assigned.
        Latitude	Decimal degrees, usually to six significant digits. Negative is South, positive is North.
        Longitude	Decimal degrees, usually to six significant digits. Negative is West, positive is East.
        Altitude	In feet.
        Timezone	Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.
        DST	Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand), N (None) or U (Unknown). See also: Help: Time
        Tz database timezone	Timezone in "tz" (Olson) format, eg. "America/Los_Angeles".
        Type	Type of the airport. Value "airport" for air terminals, "station" for train stations, "port" for ferry terminals and "unknown" if not known. In airports.csv, only type=airport is included.
        Source	Source of this data. "OurAirports" for data sourced from OurAirports, "Legacy" for old data not matched to OurAirports (mostly DAFIF), "User" for unverified user contributions. In airports.csv, only source=OurAirports is included.

        example: 507,"London Heathrow Airport","London","United Kingdom","LHR","EGLL",51.4706,-0.461941,83,0,"E","Europe/London","airport","OurAirports"
        """
        for row in reader:
            id = row[0]
            airport = row[1]
            country = row[3]
            if not id or not airport: continue

            graph[id] = {
                'airport': airport,
                'country': country,
                'destinations': list(),
                'costs': dict()
            }
                # costs: {destination: cost}

    file_path = os.path.join(current_directory, '../datasets/routes.csv')
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f)

        for row in reader:
            """
            Airline	2-letter (IATA) or 3-letter (ICAO) code of the airline.
            Airline ID	Unique OpenFlights identifier for airline (see Airline).
            Source airport	3-letter (IATA) or 4-letter (ICAO) code of the source airport.
            Source airport ID	Unique OpenFlights identifier for source airport (see Airport)
            Destination airport	3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
            Destination airport ID	Unique OpenFlights identifier for destination airport (see Airport)
            Codeshare	"Y" if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty otherwise.
            Stops	Number of stops on this flight ("0" for direct)
            Equipment	3-letter codes for plane type(s) generally used on this flight, separated by spaces

            example: BA,1355,SIN,3316,MEL,3339,Y,0,744
            """
            airport_src_id = row[3]
            airport_dest_id = row[5]

            if airport_src_id in graph and airport_dest_id in graph and airport_dest_id not in graph[airport_src_id]['destinations']:
                graph[airport_src_id]['destinations'].append(airport_dest_id)

                cost = random.randint(100, 1500)
                graph[airport_src_id]['costs'][airport_dest_id] = str(cost)

    
    graph_final = dict()

    for k, v in graph.items():
        if len(v["destinations"]): graph_final[k] = v

    return graph_final

def obtain_graph_limited(graph: dict, limit: int) -> dict:
    graph_limited = dict()

    for k, v in graph.items():
        if len(graph_limited) == limit: break
        graph_limited[k] = v

    return graph_limited
