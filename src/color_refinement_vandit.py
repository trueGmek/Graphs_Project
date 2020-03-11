from src.graph_io import *

with open("examplegraph.gr") as f:
    G = load_graph(f)
    n = len(G.vertices)

    # initial coloring - each vertex by degree
    for v in G.vertices:
        v.colornum = v.degree

    all_colors = []
    dic = {}
    dic_neighbour_v = {}
    lsOfSameColorVertices = []
    for v in G.vertices:
        if v.colornum not in all_colors:
            all_colors.append(v.colornum)  # list containing all color numbers we have after degree refinement


    def count_vertices(color):  # define this function
        i = 0
        for v in G.vertices:
            if v.colornum == color:
                i = i + 1
            if i > 1:
                return True
        return False


    for x in all_colors:
        if count_vertices(x):  # if vertices with color x>=2
            for v in G.vertices:
                if v.colornum == x:
                    lsOfSameColorVertices.append(v)

            for v in lsOfSameColorVertices:
                for w in v.neighbours:
                    if v not in dic:
                        dic[v] = {}
                    if w.colornum not in dic[v]:
                        dic[v][w.colornum] = 0
                    dic[v][w.colornum] += 1
            for key in dic:
                if dic[key] not in dic_neighbour_v:
                    dic_neighbour_v[dic[key]] = []
                dic_neighbour_v[dic[key]].append(key)

            for key, item in dic_neighbour_v:
                for v in item:
                    v.colornum = max(all_colors) + 1
                all_colors.append(max(all_colors) + 1)

            for v in G.vertices:
                for i in range(max(all_colors) + 1):
                    dic[v] = {i: 0}

        else:
            continue

    with open("color_refined_graph.dot", 'w') as g:
        write_dot(G, g)
