import Graph


class DirGraph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.weights = {}
        self.ref = {}

    def add_node(self, *nodes: str):
        for node in nodes:
            if node not in self.nodes:
                self.nodes.append(node)
                self.ref[node] = Node(node)

    def add_edge(self, parent: str, child: str, weight=1.0):
        p = self.ref[parent]
        c = self.ref[child]
        p.add_child(c)
        c.add_parent(p)
        self.edges.append((p, c))
        self.weights[(p, c)] = weight

    def moralize(self):
        for node in self.ref.values():
            if len(node.parents) >= 2:
                for i in range(len(node.parents)):
                    for j in range(i + 1, len(node.parents)):
                        if (node.parents[i], node.parents[j]) not in self.edges and (node.parents[j], node.parents[i]) \
                                not in self.edges:
                            self.add_edge(node.parents[i].label, node.parents[j].label)

    def get_moral_graph(self):
        self.moralize()
        moral_graph = Graph.Graph()
        for edge in self.edges:
            moral_graph.add_node(edge[0].label, edge[1].label)
            moral_graph.add_edge(edge[0].label, edge[1].label)
        return moral_graph


class Node:
    def __init__(self, name):
        self.label = name
        self.parents = []
        self.children = []

    def add_parent(self, node):
        if node.label not in self.parents:
            self.parents.append(node)

    def add_child(self, node):
        if node.label not in self.children:
            self.children.append(node)
