class Graph:
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

    def add_edge(self, n1: str, n2: str, weight=1.0):
        _n1 = self.ref[n1]
        _n2 = self.ref[n2]
        _n1.add_neighbor(_n2)
        _n2.add_neighbor(_n1)
        self.edges.append((_n1, _n2))
        self.edges.append((_n2, _n1))
        self.weights[(_n1, _n2)] = weight
        self.weights[(_n2, _n1)] = weight

    def make_chordal(self):
        alpha = {node: 0 for node in self.nodes}
        chords = set()
        weight = {node: 0 for node in self.nodes}
        unnumbered_nodes = self.nodes
        for i in range(len(self.nodes), 0, -1):
            z = max(unnumbered_nodes, key=lambda node: weight[node])
            unnumbered_nodes.remove(z)
            alpha[z] = i
            update_nodes = []
            for y in unnumbered_nodes:
                if (self.ref[y], self.ref[z]) in self.edges or (self.ref[z], self.ref[y]) in self.edges:
                    update_nodes.append(y)
                else:
                    y_weight = weight[y]
                    lower_nodes = [node for node in unnumbered_nodes if weight[node] < y_weight]
                    if self.has_path():
                        pass

    def has_path(self, source, target, subgraph=None):
        if target == source:
            return True
        if subgraph is None:
            pred = {self.ref[source]: None}
            succ = {self.ref[target]: None}

            forward_fringe = [self.ref[source]]
            reverse_fringe = [self.ref[target]]

            while forward_fringe and reverse_fringe:
                if len(forward_fringe) <= len(reverse_fringe):
                    this_level = forward_fringe
                    forward_fringe = []
                    for node in this_level:
                        for w in node.neighbors:
                            if w not in pred:
                                forward_fringe.append(w)
                                pred[w] = node
                            if w in succ:
                                return True

                else:
                    this_level = reverse_fringe
                    reverse_fringe = []
                    for node in this_level:
                        for w in node.neighbors:
                            if w not in succ:
                                succ[w] = node
                                reverse_fringe.append(w)
                            if w in pred:
                                return True

            return False
        else:
            pred = {subgraph.ref[source]: None}
            succ = {subgraph.ref[target]: None}

            forward_fringe = [subgraph.ref[source]]
            reverse_fringe = [subgraph.ref[target]]

            while forward_fringe and reverse_fringe:
                if len(forward_fringe) <= len(reverse_fringe):
                    this_level = forward_fringe
                    forward_fringe = []
                    for node in this_level:
                        for w in [x for x in node.neighbors if x in subgraph.ref.values()]:
                            if w not in pred:
                                forward_fringe.append(w)
                                pred[w] = node
                            if w in succ:
                                return True

                else:
                    this_level = reverse_fringe
                    reverse_fringe = []
                    for node in this_level:
                        for w in [x for x in node.neighbors if x in subgraph.ref.values()]:
                            if w not in succ:
                                succ[w] = node
                                reverse_fringe.append(w)
                            if w in pred:
                                return True

            return False

    def subgraph(self, nodes: list):
        sub = Graph()
        for node in self.nodes:
            if node in nodes:
                sub.ref[node] = self.ref[node]
        for edge in self.edges:
            if edge[0] in [sub.ref[node] for node in sub.nodes] and edge[1] in [sub.ref[node] for node in sub.nodes]:
                sub.edges.append(edge)
        return sub


class Node:
    def __init__(self, name):
        self.label = name
        self.neighbors = []

    def add_neighbor(self, node):
        if node.label not in self.neighbors:
            self.neighbors.append(node)
