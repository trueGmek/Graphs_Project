import itertools as iter
import os
from src.graph_io import *


def get_coloring(graph):
    coloring = {}
    for v in graph.vertices:
        if v.colornum not in coloring:
            coloring[v.colornum] = v.colornum
        else:
            coloring[v.colornum] += 1
    return coloring


def have_identically_colored_neighbourhoods(u, v):
    if u.degree != v.degree:
        return False
    for neighbour_u in u.neighbours:
        for neighbour_v in v.neighbours:
            if not (neighbour_u.colornum == neighbour_v.colornum and neighbour_u != neighbour_v):
                return False
    return True


def color_refinement(graph):
    G = graph
    n = len(G.vertices)
    for v in G.vertices:
        v.colornum = v.degree
    i = 0
    while True:
        i += 1
        previous_coloring = get_coloring(G)
        for u, v in iter.combinations(G.vertices, 2):
            if u.colornum == v.colornum and not have_identically_colored_neighbourhoods(u, v):
                u.colornum = n + i + 1
        curr_coloring = get_coloring(G)
        if previous_coloring == curr_coloring:
            break
    return G


def test_color_refinement():
    open_path = os.path.relpath('../graphs/examplegraph_2.gr', os.path.dirname(__file__))
    with open(open_path, 'r') as f:
        G = load_graph(f)
        result = color_refinement(G)
        save_path = os.path.relpath('../graphs/color_refined_examplegraph_2.dot', os.path.dirname(__file__))
        with open(save_path, 'w') as g:
            write_dot(result, g)
