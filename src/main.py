import graphviz
import DirGraph as dg
import json

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
    f = open('setup.json')
    j = json.load(f)["medium"]
    dg = dg.DirGraph()
    dg.parseFromJson(j)
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
