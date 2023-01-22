import graphviz
import DirGraph as dg

# Per salvare i file da visualizzare utilizzare questa directory
# render(directory='../doctest-output', view=True)


def vis_dgraph(grph, fname='Directed Graph'):
    dot = graphviz.Digraph(fname)
    for node in grph.ref.keys():
        dot.node(node)
    for edge in grph.edges:
        dot.edge(edge[0].label, edge[1].label)
    dot.render(directory='../doctest-output', view=True)


def vis_graph(grph, fname='Undirected Graph'):
    dot = graphviz.Graph(fname)
    for node in grph.nodes:
        dot.node(node)
    edges = [edge for edge in grph.edges]
    for edge in edges:
        dot.edge(edge[0].label, edge[1].label)
        edges.remove((edge[1], edge[0]))
    dot.render(directory='../doctest-output', view=True)


def vis_jgraph(grph, fname='Junction Graph'):
    dot = graphviz.Graph(fname)
    for node in grph.nodes:
        if grph.ref[node].type == 'Separator':
            dot.node(node, _attributes={'shape': 'square'})
        else:
            dot.node(node)
    edges = [edge for edge in grph.edges]
    for edge in edges:
        dot.edge(edge[0].label, edge[1].label)
        edges.remove((edge[1], edge[0]))
    dot.render(directory='../doctest-output', view=True)


if __name__ == '__main__':
    dg = dg.DirGraph()
    dg.add_node('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
    dg.add_edge('A', 'B')
    dg.add_edge('A', 'C')
    dg.add_edge('A', 'D')
    dg.add_edge('B', 'E')
    dg.add_edge('C', 'F')
    dg.add_edge('D', 'G')
    dg.add_edge('E', 'H')
    dg.add_edge('F', 'H')
    dg.add_edge('F', 'I')
    dg.add_edge('G', 'I')
    vis_dgraph(dg, 'Starting Graph')
    mg = dg.get_moral_graph()
    vis_graph(mg, 'Moralized')
    mg.make_chordal()
    # mg.elimination_game()
    vis_graph(mg, 'Triangulated')
    mg.Bron_Kerbosch_no_pivot([], mg.nodes[:], [])
    jg = mg.get_junction_graph()
    vis_jgraph(jg, 'Junction')
    jt = jg.get_maximal_weight_spanning_tree()
    vis_jgraph(jt, 'Junction Tree')
