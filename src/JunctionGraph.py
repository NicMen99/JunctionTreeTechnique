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

    def get_maximal_weight_spanning_tree(self):
        # preparazione per uso Kruskal
        separators = [x for x in self.ref.values() if x.type == 'Separator']
        for x in separators:
            for i in range(len(x.neighbors)):
                for j in range(i + 1, len(x.neighbors)):
                    if (x.neighbors[i], x.neighbors[j]) not in self.l_edges.keys() or \
                            len(self.l_edges[(x.neighbors[i], x.neighbors[j])]) < len(x.label):
                        self.l_edges[(x.neighbors[i], x.neighbors[j])] = x.label
                        self.l_edges[(x.neighbors[j], x.neighbors[i])] = x.label
        # algoritmo di kruskal che restituisce i rami dell'albero
        tree_edges = self.kruskal()
        selected_separators = set()
        for edge in tree_edges:
            selected_separators.add(self.l_edges[edge])

        # costruzione dell'albero finale
        jt = JunctionGraph()
        for label in selected_separators:
            jt.add_node((label, 'Separator'))
        for node in self.nodes:
            if self.ref[node].type == 'Supernode':
                jt.add_node((node, 'Supernode'))
        for edge in self.edges:
            if (edge[0].label in jt.nodes and edge[1].label in jt.nodes) and (edge[0], edge[1]) not in jt.edges:
                jt.add_edge(edge[0].label, edge[1].label)
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
        for edge in self.l_edges:
            a = None
            b = None
            for i in range(len(nodesets)):
                if edge[0].label in nodesets[i]:
                    a = i
                if edge[1].label in nodesets[i]:
                    b = i
            if a != b:
                nodesets[a] = nodesets[a].union(nodesets[b])
                nodesets.pop(b)
                final_edges.add(edge)
                final_edges.add((edge[1], edge[0]))
        return final_edges


class Node:
    def __init__(self, label: str, node_type: str):
        self.label = label
        self.neighbors = []
        self.type = node_type  # i tipi sono 'Supernode' e 'Separator'

    def add_neighbor(self, node):
        if node.label not in self.neighbors:
            self.neighbors.append(node)
