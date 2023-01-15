import graphviz
import Graph as g
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


if __name__ == '__main__':
    gr = g.Graph()
    gr.add_node('A', 'B', 'C', 'D', 'E')
    gr.add_edge('A', 'B')
    gr.add_edge('A', 'C')
    gr.add_edge('A', 'D')
    gr.add_edge('C', 'B')
    gr.add_edge('C', 'D')
    gr.add_edge('C', 'E')
    gr.add_edge('B', 'E')
    gr.add_edge('D', 'E')
    vis_graph(gr)
    gr.make_chordal()
    vis_graph(gr, 'Triangular')
    gr.Bron_Kerbosch_no_pivot([], gr.nodes, [])
    print("debug")
