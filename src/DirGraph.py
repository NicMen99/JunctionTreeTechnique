import Graph


class DirGraph:
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

    def add_edge(self, parent, child, weight=1.0):
        self.add_node(parent, child)
        parent.add_child(child)
        child.add_parent(parent)
        self.edges.append((parent, child))
        self.weights[(parent, child)] = weight

    def moralize(self):
        for node in self.nodes:
            if len(node.parents) >= 2:
                for i in range(len(node.parents)):
                    for j in range(i + 1, len(node.parents)):
                        if (node.parents[i], node.parents[j]) not in self.edges and (node.parents[j], node.parents[i]) \
                                not in self.edges:
                            self.add_edge(node.parents[i], node.parents[j])

    def get_moral_graph(self):
        self.moralize()
        moral_graph = Graph.Graph()

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
