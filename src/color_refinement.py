import os

from src.graph_io import *


def color_refinement(in_graph):
    all_colors = []
    dictionary_vertices_neighbour_colors = {}
    number_of_verticies = len(in_graph.vertices)

    for v in in_graph.vertices:
        if v.colornum not in all_colors:
            all_colors.append(v.colornum)

    different_colors = len(all_colors)

    for v in in_graph.vertices:
        dictionary_vertices_neighbour_colors[v.label] = {}

    for v in in_graph.vertices:
        for i in range(number_of_verticies + different_colors + 1):
            dictionary_vertices_neighbour_colors[v.label][i] = 0

    for color in all_colors:
        if color <= (number_of_verticies + different_colors):
            ls_of_same_color_vertices = []
            if count_vertices(color, in_graph):  # if vertices with color x>=2
                for v in in_graph.vertices:
                    if v.colornum == color:
                        ls_of_same_color_vertices.append(v)

                for v in ls_of_same_color_vertices:
                    for w in v.neighbours:
                        if w.colornum not in dictionary_vertices_neighbour_colors[v.label]:
                            with open("color_refined_graph.dot", 'w') as g:
                                write_dot(in_graph, g)
                            exit()
                        else:
                            dictionary_vertices_neighbour_colors[v.label][w.colornum] += 1

                seen_array = []
                group_array = []

                for v in ls_of_same_color_vertices:
                    if v.label not in seen_array:
                        group_of_this = [v.label]
                        seen_array.append(v.label)
                        for k2, val2 in dictionary_vertices_neighbour_colors.items():
                            if dictionary_vertices_neighbour_colors[v.label] == val2 and k2 not in seen_array:
                                group_of_this.append(k2)
                                seen_array.append(k2)

                        group_array.append(group_of_this)

                for j in range(len(group_array)):
                    for i in group_array[j]:
                        for v in in_graph.vertices:
                            if v.label == i:
                                v.colornum = max(all_colors) + 1

                    for v in ls_of_same_color_vertices:
                        if v.colornum not in all_colors:
                            all_colors.append(v.colornum)
            else:
                continue
        else:
            break
    return in_graph


def initialize_colornum(graph):
    for v in graph.vertices:
        v.colornum = v.degree
    return graph


def count_vertices(color, in_graph):
    i = 0
    for v in in_graph.vertices:
        if v.colornum == color:
            i = i + 1
        if i > 1:
            return True
    return False


def test_color_refinement():
    cur_path = os.path.dirname(__file__)
    new_path = os.path.relpath('../graphs/example_balanced_graph_1.gr', cur_path)

    with open(new_path, 'r') as file_stream:
        graph_from_file = load_graph(file_stream)

    initialize_colornum(graph_from_file)
    output_graph = color_refinement(graph_from_file)

    with open("color_refined_graph.dot", 'w') as file_stream:
        write_dot(output_graph, file_stream)
