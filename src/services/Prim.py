import heapq

class CPrim:
    def __init__(self, grafo, nodo_inicial, nodo_final):
        self.grafo = grafo
        self.visitados = set()
        self.mst = []       # Stores the edges in the MST
        self.aristas = []   # Priority queue for edges
        self.nodo_inicial = nodo_inicial
        self.nodo_final = nodo_final
        self.agregar_aristas(nodo_inicial)

    def agregar_aristas(self, nodo):
        for destino, costo in self.grafo[nodo].items():
            # Convert cost to integer
            costo = int(costo)
            if destino not in self.visitados:
                heapq.heappush(self.aristas, (costo, nodo, destino))

        self.visitados.add(nodo)

    def prim(self):
        while self.aristas:
            costo, origen, destino = heapq.heappop(self.aristas)
            if destino not in self.visitados:
                self.visitados.add(destino)
                self.mst.append((origen, destino, costo))
                
                # Add edges of the newly visited node
                if destino in self.grafo:
                    self.agregar_aristas(destino)
                
                # Stop if we reach the target node
                if destino == self.nodo_final:
                    break

    def obtener_camino(self):
        camino = []
        actual = self.nodo_final
        while actual != self.nodo_inicial:
            for origen, destino, _ in reversed(self.mst):
                if destino == actual:
                    camino.insert(0, actual)
                    actual = origen
                    break
        camino.insert(0, self.nodo_inicial)
        return camino
    
    def obtener_costo(self):
        return sum(costo for _, _, costo in self.mst)

"""
grafo = {
    "A": {"B": 31, "C" : 36, "G": 43},
    "B": {"A": 31, "C": 37, "D": 35, "F": 44, "G": 40},
    "C": {"A": 36, "B": 37, "D": 33, "E": 53, "H": 58},
    "D": {"B": 35, "C": 33, "E": 42},
    "E": {"C": 53, "D": 42, "F": 48, "H": 41},
    "F": {"B": 44, "E": 48, "G": 39, "H": 46},
    "G": {"A": 43, "B": 40, "F": 39, "H": 44},
    "H": {"C": 58, "E": 41, "F": 46, "G": 44}
}

prim = CPrim(grafo, "A")
prim.prim()

print("Arbol de expansion minima:")
for origen, destino, costo in prim.mst:
    print(f"{origen} -> {destino} con costo {costo}")

costo_minimo = sum(costo for _, _, costo in prim.mst)

print(f"Costo minimo: {costo_minimo}")
"""