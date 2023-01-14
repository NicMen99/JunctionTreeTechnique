import graphviz
import DirGraph as dg


# Per salvare i file da visualizzare utilizzare questa directory
# render(directory='../doctest-output', view=True)


def vis_dgraph(grph):
    dot = graphviz.Digraph('Directed Graph')
    for node in grph.ref.keys():
        dot.node(node)
    for edge in grph.edges:
        dot.edge(edge[0].label, edge[1].label)
    dot.render(directory='../doctest-output', view=True)


def vis_graph(grph):
    dot = graphviz.Graph('Moralized Undirected Graph')
    for node in grph.nodes:
        dot.node(node)
    edges = [edge for edge in grph.edges]
    for edge in edges:
        dot.edge(edge[0].label, edge[1].label)
        edges.remove((edge[1], edge[0]))
    dot.render(directory='../doctest-output', view=True)


if __name__ == '__main__':
    graph = dg.DirGraph()
    graph.add_node('A', 'B', 'C', 'D', 'E', 'F')
    graph.add_edge('A', 'B')
    graph.add_edge('A', 'C')
    graph.add_edge('B', 'D')
    graph.add_edge('C', 'E')
    graph.add_edge('E', 'F')
    graph.add_edge('D', 'F')
    vis_dgraph(graph)
    graph = graph.get_moral_graph()
    vis_graph(graph)
    graph.make_chordal()
    vis_graph(graph)

