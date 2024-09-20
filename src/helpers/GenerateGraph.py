from pyvis.network import Network
import networkx as nx

def generate_graph_image(graph):
    """
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B", "D"],
    }
    """
    nx_graph = nx.cycle_graph(len(graph))
    nx_graph = nx.relabel_nodes(nx_graph, graph)

    nt = Network("500px", "500px")
    nt.from_nx(nx_graph)
    nt.show("graph.html")
    