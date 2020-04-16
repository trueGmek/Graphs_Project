import os
from queue import Queue

from src.graph_io import *


def get_coloring(graph):
    coloring = {}
    for v in graph.vertices:
        if v.colornum not in coloring:
            coloring[v.colornum] = 1
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


def count_nr_of_neighbors_of_color(vertices, col):
    result = {}
    for v in vertices:
        result[v] = 0
        for u in v.neighbours:
            if u.colour == col:
                result[v] += 1
    return result


def color_refinement(graph):
    initial_coloring = [v.degree for v in graph.vertices]
    vertices_of_color = {1: graph.vertices}
    c_min = 1
    c_max = 1
    colors = Queue()
    colors.put(1)

    while colors:
        c = colors.get()
        # count nr of neighbors of color c of every vertex
        d = count_nr_of_neighbors_of_color(graph.vertices, c)
        # ordered partition of vertices v sorted by (initial coloring, num of neighbours of color c)
        b = sorted(vertices_of_color, key=lambda i: (initial_coloring, d))
        for i in range(c_min, c_max):
            k1, k2 = 0, len(b)
            if i != max(b):
                colors.put(i)
        c_min = c_max + 1
        c_max += len(b)
        for x in range(c_min, c_max):
            vertices_of_color[x] = b[x + 1 - c_min]
            initial_coloring = [x for x in vertices_of_color[x]]
    return initial_coloring


def test_color_refinement():
    open_path = os.path.relpath('../graphs/examplegraph_2.gr', os.path.dirname(__file__))
    with open(open_path, 'r') as f:
        G = load_graph(f)
        result = color_refinement(G)
        save_path = os.path.relpath('../graphs/color_refined_examplegraph_2.dot', os.path.dirname(__file__))
        with open(save_path, 'w') as g:
            write_dot(result, g)
