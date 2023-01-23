class JunctionGraph:
    def __init__(self):
        self.nodes = []
        self.edges = set()
        self.l_edges = {}
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
        self.edges.add((_n1, _n2))
        self.edges.add((_n2, _n1))

    def add_labeled_edge(self, n1: str, n2: str, label: str):
        self.add_edge(label, n1)
        self.add_edge(label, n2)
        _n1 = self.ref[n1]
        _n2 = self.ref[n2]
        _n1.add_neighbor(_n2)
        _n2.add_neighbor(_n1)
        self.l_edges[(_n1, _n2)] = label
        self.l_edges[(_n2, _n1)] = label

    def get_maximal_weight_spanning_tree(self):
        # algoritmo di kruskal che restituisce i rami dell'albero
        tree_edges = self.kruskal()

        # costruzione dell'albero finale
        jt = JunctionGraph()
        for node in self.nodes:
            if self.ref[node].type == 'Supernode':
                jt.add_node((node, 'Supernode'))
        for edge in tree_edges:
            jt.add_node((edge[1], 'Separator'))
            jt.add_labeled_edge(edge[0][0].label, edge[0][1].label, edge[1])
        return jt

    def kruskal(self):
        final_edges = set()
        nodesets = []
        # ordinamento degli archi del grafo per peso
        self.l_edges = dict(sorted(self.l_edges.items(), key=lambda item: len(item[1]), reverse=True))
        for node in self.nodes:
            if self.ref[node].type == 'Supernode':
                _set = set()
                _set.add(node)
                nodesets.append(_set)
        for edge in self.l_edges.items():
            a = None
            b = None
            for i in range(len(nodesets)):
                if edge[0][0].label in nodesets[i]:
                    a = i
                if edge[0][1].label in nodesets[i]:
                    b = i
            if a != b:
                nodesets[a] = nodesets[a].union(nodesets[b])
                nodesets.pop(b)
                final_edges.add(edge)
        return final_edges


class Node:
    def __init__(self, label: str, node_type: str):
        self.label = label
        self.neighbors = []
        self.type = node_type  # i tipi sono 'Supernode' e 'Separator'

    def add_neighbor(self, node):
        if node.label not in self.neighbors:
            self.neighbors.append(node)
