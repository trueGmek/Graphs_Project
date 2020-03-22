from src.graph_io import *
import os


def count_vertices(color):
    i = 0
    for v in G.vertices:
        if v.colornum == color:
            i += 1
        if i > 1:
            return True
    return False


path = os.path.relpath('../graphs/examplegraph.gr', os.path.dirname(__file__))
with open(path, 'r') as f:
    G = load_graph(f)
    n = len(G.vertices)

    for v in G.vertices:
        v.colornum = v.degree

    all_colors = []
    dic = {}
    dic_neighbour_v = {}
    lsOfSameColorVertices = []

    for v in G.vertices:
        if v.colornum not in all_colors:
            all_colors.append(v.colornum)

    different_colors = len(all_colors)

    for v in G.vertices:
        dic[v.label] = {}

    for v in G.vertices:
        for i in range(n + different_colors + 1):
            dic[v.label][i] = 0

    for x in all_colors:
        if x <= (n + different_colors):
            lsOfSameColorVertices = []
            if count_vertices(x):  # if vertices with color x>=2
                for v in G.vertices:
                    if v.colornum == x:
                        lsOfSameColorVertices.append(v)

                for v in lsOfSameColorVertices:
                    for w in v.neighbours:
                        if w.colornum not in dic[v.label]:
                            with open("color_refined_graph.dot", 'w') as g:
                                write_dot(G, g)
                            exit()
                        else:
                            dic[v.label][w.colornum] += 1

                seenArray = []
                groupArray = []
                # Create a new dic
                numKey = 0
                for v in lsOfSameColorVertices:
                    if v.label not in seenArray:
                        groupOfThis = [v.label]
                        seenArray.append(v.label)
                        for k2, val2 in dic.items():
                            if dic[v.label] == val2 and k2 not in seenArray:
                                groupOfThis.append(k2)
                                seenArray.append(k2)
                        numKey += 1
                        groupArray.append(groupOfThis)

                print(all_colors)
                print(groupArray)

                for j in range(len(groupArray)):
                    for i in groupArray[j]:
                        for v in G.vertices:
                            if v.label == i:
                                v.colornum = max(all_colors) + 1

                    for v in lsOfSameColorVertices:
                        if v.colornum not in all_colors:
                            all_colors.append(v.colornum)

            else:
                continue

        else:
            break
