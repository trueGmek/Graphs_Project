import itertools as iter

from src.graph_io import *


def degree(v):
    deg = 0
    for _ in v.incidence:
        deg += 1
    return deg


with open("../examplegraph.gr") as f:
    G = load_graph(f)
    n = len(G.vertices)
    num_of_vertices_of_color = [None] * n
    color_dicts = []

    # initial coloring - each vertex by degree
    for v in G.vertices:
        v.degree = degree(v)
        for i in range(1, n - 1):
            if v.degree == i:
                v.color = i
                num_of_vertices_of_color[i] += 1

    # loop over the vertices of same color
    for l in num_of_vertices_of_color:
        if l > 1:
            v = G.vertices[l]
            same_color_neighbours = {}
            for e in G.incidence:
                w = e.other_end(v)
                w_color = w.color
                same_color_neighbours[w_color] += 1
            color_dicts.append(same_color_neighbours)

    for dict1, dict2 in iter.permutations(color_dicts, 2):
        v = G.vertices[color_dicts.index(dict1)]
        if dict1 != dict2:
            v.color = n + i

    with open("../trial.dot", 'w') as g:
        write_dot(G, g)
