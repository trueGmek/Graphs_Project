import itertools as iter

from src.graph_io import *


def get_coloring(G):
    coloring = {}
    for v in G.vertices:
        if v.colornum not in coloring:
            coloring[v.colornum] = v.colornum
        else:
            coloring[v.colornum] += 1
    return coloring


def have_identically_colored_neighbourhoods(u, v):
    if u.degree != v.degree:
        return False
    list_of_same_colored_neighbours = [False] * u.degree
    i = 0
    for neighbour_u in u.neighbours:
        for neighbour_v in v.neighbours:
            if neighbour_u.colornum == neighbour_v.colornum and neighbour_u != neighbour_v:
                list_of_same_colored_neighbours[i] = True
        i += 1
    for x in list_of_same_colored_neighbours:
        if x is False:
            return False
    return True


with open("../examplegraph.gr") as f:
    G = load_graph(f)
    n = len(G.vertices)
    num_of_vertices_of_color = [0] * n
    color_dicts = []
    changed = True

    # initial coloring - each vertex by degree
    for v in G.vertices:
        v.colornum = v.degree

    i = 0
    while True:
        i += 1
        previous_coloring = get_coloring(G)
        for u, v in iter.combinations(G.vertices, 2):
            if u.colornum == v.colornum and have_identically_colored_neighbourhoods(u, v):
                u.colornum = v.colornum
            elif u.colornum == v.colornum:
                u.colornum = n + i + 1
        curr_coloring = get_coloring(G)
        if previous_coloring == curr_coloring:
            break

    with open("../color_refined_graph.dot", 'w') as g:
        write_dot(G, g)
