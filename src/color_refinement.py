import itertools as iter

from src.graph_io import *

with open("../examplegraph.gr") as f:
    G = load_graph(f)
    n = len(G.vertices)
    num_of_vertices_of_color = [0] * n
    color_dicts = []
    changed = True

    # initial coloring - each vertex by degree
    for v in G.vertices:
        for i in range(1, n - 1):
            if v.degree == i:
                v.colornum = i
                num_of_vertices_of_color[i] += 1

    while changed:
        changed = False
        # loop over the vertices of same color
        for l in num_of_vertices_of_color:
            if l > 1:
                v = G.vertices[l]
                same_color_neighbours = {}
                for e in v.incidence:
                    w = e.other_end(v)
                    if w.colornum not in same_color_neighbours:
                        same_color_neighbours[w.colornum] = 1
                    else:
                        same_color_neighbours[w.colornum] += 1
                        changed = True
                color_dicts.append(same_color_neighbours)

        for dict1, dict2 in iter.permutations(color_dicts, 2):
            i = color_dicts.index(dict1)
            v = G.vertices[i]
            if dict1 != dict2:
                v.colornum = n + i + 1

    with open("../trial.dot", 'w') as g:
        write_dot(G, g)
