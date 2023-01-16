class JunctionGraph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.ref = {}

    def add_node(self, *nodes):
        for node in nodes:
            if node[0] not in self.nodes:
                self.nodes.append(node[0])
                self.ref[node[0]] = Node(node[0], node[1])

    def add_edge(self, n1: str, n2: str):
        _n1 = self.ref[n1]
        _n2 = self.ref[n2]
        _n1.add_neighbor(_n2)
        _n2.add_neighbor(_n1)
        self.edges.append((_n1, _n2))
        self.edges.append((_n2, _n1))


class Node:
    def __init__(self, label: str, node_type: str):
        self.label = label
        self.neighbors = []
        self.type = node_type

    def add_neighbor(self, node):
        if node.label not in self.neighbors:
            self.neighbors.append(node)