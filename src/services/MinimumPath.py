from collections import deque

class MinimumPath:
    def __init__(self):
        self.graph = {
            "A": ["B", "C"],
            "B": ["A", "D", "E"],
            "C": ["A", "F"],
            "D": ["B"],
            "E": ["B", "F"],
            "F": ["C", "E"]
        }

    def bfs(self, src: str, dest: str) -> list:
        if src not in self.graph or dest not in self.graph:
            return [f"No se encontró la ruta entre {src} y {dest}"]
        
        queue = deque([[src]])
        visited = set()

        while queue:
            path = queue.popleft()
            node = path[-1]

            if node == dest:
                return path  # Esto es una lista de nodos
            
            if node not in visited:
                visited.add(node)
                for neighbor in self.graph[node]:
                    if neighbor not in visited:
                        queue.append(path + [neighbor])

        return [f"No hay ruta disponible entre {src} y {dest}"]
   