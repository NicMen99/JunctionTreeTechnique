class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.weights = {}
        self.references = {}

    def add_node(self, *nodes):
        for node in nodes:
            if node not in self.nodes:
                self.nodes.append(node)
                self.references[node.label] = node

    def add_edge(self, n1, n2, weight=1.0):
        self.add_node(n1, n2)
        n1.add_neighbor(n2)
        n2.add_parent(n1)
        self.edges.append((n1, n2))
        self.weights[(n1, n2)] = weight


class Node:
    def __init__(self, name):
        self.label = name
        self.neighbors = []

    def add_neighbor(self, node):
        if node.label not in self.neighbors:
            self.neighbors.append(node)
