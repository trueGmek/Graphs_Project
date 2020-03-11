import itertools as iter

from src.graph_io import *


def get_coloring(G):
    coloring = {}
    for v in G.vertices:
        if v.colornum not in coloring:
            coloring[v.colornum] = 1
        else:
            coloring[v.colornum] += 1
    return coloring


def have_identically_colored_neighbourhoods(u, v):
    if u.degree != v.degree:
        return False
    coloring_u = {}

    coloring_v = {}

    for neighbour_u in u.neighbours:
        if neighbour_u.colornum not in coloring_u:
            coloring_u[neighbour_u.colornum] = 1
        else:
            coloring_u[neighbour_u.colornum] += 1

    for neighbour_v in v.neighbours:
        if neighbour_v.colornum not in coloring_v:
            coloring_v[neighbour_v.colornum] = 1
        else:
            coloring_v[neighbour_v.colornum] += 1
    if coloring_u != coloring_v:
        return False
    return True


with open("../examplegraph.gr") as f:
    G = load_graph(f)
    n = len(G.vertices)
    list_of_dicts = []
    tmp_dict = {}

    # initial coloring - each vertex by degree
    for v in G.vertices:
        v.colornum = v.degree
    i = 0
    while True:
        i += 1
        previous_coloring = get_coloring(G)
        with open("../{}.dot".format(i), 'w') as g:
            write_dot(G, g)
        j = i
        for u, v in iter.combinations(G.vertices, 2):
            if u.colornum == v.colornum and not have_identically_colored_neighbourhoods(u, v):
                tmp_dict[u.colornum] = 1
            list_of_dicts.append(tmp_dict)
        for dict1, dict2 in iter.combinations(list_of_dicts, 2):
            if dict1 != dict2:

        curr_coloring = get_coloring(G)
        if previous_coloring == curr_coloring:
            break

    with open("../color_refined_graph.dot", 'w') as g:
        write_dot(G, g)
