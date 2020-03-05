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

    # initial coloring - each vertex by degree
    for v in G.vertices:
        v.degree = degree(v)
        for i in range(1, n - 1):
            if v.degree == i:
                v.color = i
                num_of_vertices_of_color[i] += 1

    # loop over the num of vertices with same color
    for l in num_of_vertices_of_color:
        if l > 1:
            for j in range(l):
                same_color_neighbours = {}
                v = G.vertices[j]
                for e in G.edges:
                    w = e.other_end(v)
                    same_color_neighbours[i] += 1
