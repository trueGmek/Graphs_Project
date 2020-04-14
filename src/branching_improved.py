import os

from src.branching import read_list_of_graphs_from_file
from src.graph_io import write_dot, load_graph
from src.graph import *


# graphs = read_list_of_graphs_from_file('../graphs/branching/lecture_graphs.grl')


def test_improved_branching():
    open_path = os.path.relpath("../graphs/branching/lecture_graphs.grl", os.path.dirname(__file__))

    with open(open_path, 'r') as file:
        L = load_graph(file, Graph, True)
    graphs = L[0]

    print(graphs[0].edges)
    print(graphs[1].edges)

    disjointed_graph = graphs[1] + graphs[0]

    print(disjointed_graph.edges)
    count_isomorphism(graphs[0].vertices, graphs[1].vertices, graphs[0] + graphs[1])

    with open("color_refined_graph.dot", 'w') as file_stream:
        write_dot(disjointed_graph, file_stream)

    with open("graphs[1]_+_graphs[0].dot", 'w') as file_stream:
        write_dot(graphs[1] + graphs[0], file_stream)


def count_isomorphism(D, I, disjoint_union):
    pass
# print(D, '\n', '\n', I, '\n', disjoint_union.edges)
