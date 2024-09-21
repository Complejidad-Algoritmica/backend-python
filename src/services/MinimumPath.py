# src/services/MinimumPath.py
from collections import deque
from .GenerateDataset import *  # Debe ser en minúsculas

class MinimumPath:
    def __init__(self):
        self.grafo = crear_grafo_con_destinos()
        self.grafo_limitado = obtain_graph_limited(self.grafo, 1500)
        descargar_grafo(self.grafo_limitado)

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
    
    def dfs(self, graph: dict, start: str, end: str, path: list, all_paths: list):
        path = path + [start]

        if start == end:
            all_paths.append(path)
            return
        
        if len(path) > 4 or len(all_paths) > 50:
            return
        
        for neighbor in graph[start]["destinations"]:
            if neighbor not in path:
                self.dfs(graph, neighbor, end, path, all_paths)

    def obtain_all_paths(self, src: str, dest: str) -> list:
        all_paths = list()
        self.dfs(self.grafo, src, dest, [], all_paths)

        return all_paths
        
    def obtain_paths_with_names(self, all_paths: list) -> list:
        paths_with_names = list()

        for path in all_paths:
            path_name = list()
            for id in path:
                path_name.append(self.grafo[id]["airport"])

            paths_with_names.append(path_name)
        return paths_with_names
