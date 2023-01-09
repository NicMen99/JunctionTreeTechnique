import graphviz
import DirGraph as dg


# Per salvare i file da visualizzare utilizzare questa directory
# render(directory='../doctest-output', view=True)


def vis_dgraph(grph):
    dot = graphviz.Digraph('Directed Graph')
    for node in grph.references.keys():
        dot.node(node)
    for edge in grph.edges:
        dot.edge(edge[0].label, edge[1].label)
    dot.render(directory='../doctest-output', view=True)


def vis_graph(grph):
    dot = graphviz.Graph('Moralized Undirected Graph')
    for node in grph.nodes:
        dot.node(node)
    for edge in grph.edges:
        dot.edge(edge[0].label, edge[1].label)
    dot.render(directory='../doctest-output', view=True)


if __name__ == '__main__':
    graph = dg.DirGraph()
    graph.add_node('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'C')
    graph.add_edge('D', 'E')
    graph.add_edge('C', 'E')
    graph.add_edge('C', 'F')
    graph.add_edge('E', 'G')
    graph.add_edge('E', 'H')
    vis_dgraph(graph)
    m_graph = graph.get_moral_graph()
    vis_graph(m_graph)
