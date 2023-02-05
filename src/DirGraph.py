import Graph

class DirGraph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.ref = {}

    def add_node(self, *nodes: str):
        for node in nodes:
            if node not in self.nodes:
                self.nodes.append(node)
                self.ref[node] = Node(node)

    def add_edge(self, parent: str, child: str):
        p = self.ref[parent]
        c = self.ref[child]
        p.add_child(c)
        c.add_parent(p)
        self.edges.append((p, c))

    def parseFromJson(self, json):
        for n in json["nodes"]:
            self.add_node(n)
        for a in json["arcs"]:
            self.add_edge(a.split("-")[0], a.split("-")[1])

    def moralize(self):
        new_arcs = []
        for node in self.ref.values():
            if len(node.parents) >= 2:
                for i in range(len(node.parents)):
                    for j in range(i + 1, len(node.parents)):
                        if (node.parents[i], node.parents[j]) not in self.edges and (node.parents[j], node.parents[i]) \
                                not in self.edges:
                            new_arcs.append((node.parents[i].label, node.parents[j].label))
        return new_arcs

    def get_moral_graph(self):
        moral_arcs = self.moralize()
        moral_graph = Graph.Graph()
        for edge in self.edges:
            moral_graph.add_node(edge[0].label, edge[1].label)
            moral_graph.add_edge(edge[0].label, edge[1].label)
        for a in moral_arcs:
            moral_graph.add_edge(a[0], a[1])
        return moral_graph


class Node:
    def __init__(self, name: str):
        self.label = name
        self.parents = []
        self.children = []

    def add_parent(self, node):
        if node.label not in self.parents:
            self.parents.append(node)

    def add_child(self, node):
        if node.label not in self.children:
            self.children.append(node)
