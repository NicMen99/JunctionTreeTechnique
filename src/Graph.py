from src import JunctionGraph


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.ref = {}
        self.cliques = []

    def add_node(self, *nodes: str):
        for node in nodes:
            if node not in self.nodes:
                self.nodes.append(node)
                self.ref[node] = Node(node)

    def add_edge(self, n1: str, n2: str):
        _n1 = self.ref[n1]
        _n2 = self.ref[n2]
        _n1.add_neighbor(_n2)
        _n2.add_neighbor(_n1)
        self.edges.append((_n1, _n2))
        self.edges.append((_n2, _n1))

    def make_chordal(self):
        # alpha = {node: 0 for node in self.nodes}
        chords = set()
        weight = {node: 0 for node in self.nodes}
        unnumbered_nodes = []
        for i in self.nodes:
            unnumbered_nodes.append(i)
        for i in range(len(self.nodes), 0, -1):
            z = max(unnumbered_nodes, key=lambda node: weight[node])
            unnumbered_nodes.remove(z)
            # alpha[z] = i
            update_nodes = []
            for y in unnumbered_nodes:
                if (self.ref[y], self.ref[z]) in self.edges or (self.ref[z], self.ref[y]) in self.edges:
                    update_nodes.append(y)
                else:
                    y_weight = weight[y]
                    lower_nodes = [node for node in unnumbered_nodes if weight[node] < y_weight]
                    if self.has_path(y, z, subgraph=self.subgraph(lower_nodes + [y, z])):
                        update_nodes.append(y)
                        chords.add((z, y))
            for node in update_nodes:
                weight[node] += 1
        for i in chords:
            self.add_edge(i[0], i[1])

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

    def Bron_Kerbosch_no_pivot(self, R: list, P: list, X: list):
        if len(P) == 0 and len(X) == 0:
            self.cliques.append(R)
            return
        for v in P[:]:
            r = R[::]
            r.append(v)
            p = [i for i in P if self.ref[i] in self.ref[v].neighbors]
            x = [j for j in X if self.ref[j] in self.ref[v].neighbors]
            self.Bron_Kerbosch_no_pivot(r, p, x)
            P.remove(v)
            X.append(v)

    def get_junction_graph(self):
        g = JunctionGraph.JunctionGraph()
        for c in self.cliques:
            label = ''
            for s in c:
                label = label + s
            g.add_node((label, 'Supernode'))

        supernodes = g.nodes[:]
        for i in range(len(supernodes)):
            for j in range(i+1, len(supernodes)):
                inter = [element for element in supernodes[i] if element in supernodes[j]]
                label = ''
                if len(inter):
                    for k in inter:
                        label = label + k
                    g.add_node((label, 'Separator'))
                    if (g.ref[label], g.ref[supernodes[i]]) not in g.edges:
                        g.add_edge(label, supernodes[i])
                    if (g.ref[label], g.ref[supernodes[j]]) not in g.edges:
                        g.add_edge(label, supernodes[j])

        return g

    # def is_chordal(self): TODO

    # TODO aggiungere metodo di triangolazione come specificato su HUGINS 4.5.3


class Node:
    def __init__(self, name: str):
        self.label = name
        self.neighbors = []

    def add_neighbor(self, node):
        if node.label not in self.neighbors:
            self.neighbors.append(node)
