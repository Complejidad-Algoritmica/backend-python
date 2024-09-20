# src/services/MinimumPath.py
from collections import deque
from ..routes.GenerateDataset import grafo  # Debe ser en minúsculas

class MinimumPath:
    def __init__(self):
        self.grafo = grafo  # Asignar el grafo a la instancia

    def bfs(self, src: str, dest: str) -> list:
        if src not in self.grafo or dest not in self.grafo:
            return []  # Retornar vacío si el origen o destino no están en el grafo

        queue = deque([src])
        visited = {src: None}

        while queue:
            current = queue.popleft()

            if current == dest:
                path = []
                while current is not None:
                    path.append(current)
                    current = visited[current]
                return path[::-1]  # Retornar el camino en orden correcto

            for neighbor in self.grafo[current]:
                if neighbor not in visited:
                    visited[neighbor] = current
                    queue.append(neighbor)

        return []  # Retornar vacío si no hay camino
