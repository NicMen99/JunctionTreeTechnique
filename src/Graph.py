class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.weights = {}
        self.references = {}

    def add_node(self, *nodes: str):
        for node in nodes:
            if node not in self.nodes:
                self.nodes.append(node)
                self.references[node] = Node(node)

    def add_edge(self, n1: str, n2: str, weight=1.0):
        _n1 = self.references[n1]
        _n2 = self.references[n2]
        _n1.add_neighbor(_n2)
        _n2.add_neighbor(_n1)
        self.edges.append((_n1, _n2))
        self.weights[(_n1, _n2)] = weight


class Node:
    def __init__(self, name):
        self.label = name
        self.neighbors = []

    def add_neighbor(self, node):
        if node.label not in self.neighbors:
            self.neighbors.append(node)
