from pyvis.network import Network
import os

def generate_graph_image(graph):
    """
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B", "D"],
    }
    """
    net = Network(notebook=True)

    for node, neighbors in graph.items():
        for neighbor in neighbors:
            net.add_node(node)         
            net.add_node(neighbor)    
            net.add_edge(node, neighbor) 

    current_path = os.path.dirname(__file__)
    file_path = os.path.join(current_path, '../img/graph.html')

    net.write_html(file_path)

def order_graph_prim(graph: dict) -> dict:
    graph_ordered = dict()
    for k, v in graph.items():
        graph_ordered[k] = v["costs"]

    return graph_ordered