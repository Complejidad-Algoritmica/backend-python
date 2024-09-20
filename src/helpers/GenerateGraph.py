import networkx as nx
import matplotlib.pyplot as plt

def generate_graph_image(graph):
    """
    graph = {
        "A": ["B", "C"],
        "B": ["A", "C"],
        "C": ["A", "B", "D"],
    }
    """

    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)


    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=1000, node_color='lightblue', edge_color='gray', width=2, arrows=True)

    plt.savefig('graph.png', bbox_inches='tight')
    plt.show()
    

    