import graphviz
import DirGraph as dg


# Per salvare i file da visualizzare utilizzare questa directory
# render(directory='../doctest-output', view=True)


def vis_dgraph(grph):
    dot = graphviz.Digraph('test')
    for node in grph.nodes:
        dot.node(node.label)
    for edge in grph.edges:
        dot.edge(edge[0].label, edge[1].label)
    dot.render(directory='../doctest-output', view=True)


def vis_dgraph(dgrph):
    dot = graphviz.Digraph('test')
    for node in dgrph.nodes:
        dot.node(node.label)
    for edge in dgrph.edges:
        dot.edge(edge[0].label, edge[1].label)
    dot.render(directory='../doctest-output', view=True)


def vis_graph(grph):
    dot = graphviz.Graph('test')
    for node in grph.nodes:
        dot.node(node.label)
    for edge in grph.edges:
        dot.edge(edge[0].label, edge[1].label)
    dot.render(directory='../doctest-output', view=True)


if __name__ == '__main__':
    graph = dg.DirGraph()
    A = dg.Node('A')
    B = dg.Node('B')
    C = dg.Node('C')
    D = dg.Node('D')
    E = dg.Node('E')
    F = dg.Node('F')
    G = dg.Node('G')
    H = dg.Node('H')
    graph.add_node(A, B, C, D, E, F, G, H)
    graph.add_edge(A, C)
    graph.add_edge(B, C)
    graph.add_edge(D, E)
    graph.add_edge(C, E)
    graph.add_edge(C, F)
    graph.add_edge(E, G)
    graph.add_edge(E, H)
    vis_dgraph(graph)
    m_graph = graph.get_moral_graph()
    vis_graph(m_graph)
