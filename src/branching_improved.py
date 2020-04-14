from random import choice

from src.branching import read_list_of_graphs_from_file
from src.color_class import ColorClass
from src.color_refinement import color_refinement
from src.graph import Graph
from src.partition_refinement import partition_refinement, partition_refinement_two

from src.graph_io import write_dot


def test_improved_branching():
    graphs = read_list_of_graphs_from_file('../graphs/branching/lecture_graphs.grl')
    disjoint_graph = Graph(False)
    disjoint_graph = disjoint_graph + graphs[0]
    disjoint_graph = disjoint_graph + graphs[1]

    highest_colornum = 0
    for vertex in disjoint_graph.vertices:
        vertex.colornum = vertex.degree
        if vertex.colornum > highest_colornum:
            highest_colornum = vertex.colornum + 1

    print(count_isomorphism([], [], disjoint_graph, highest_colornum, 0))


def count_isomorphism(D, I, disjoint_union, highest_colornum, ka):
    print("NEW RECURSION\n", "HIGHEST COLORNUM: ", highest_colornum)
    for i in range(len(D)):
        D[i].colornum = highest_colornum
        I[i].colornum = highest_colornum
        highest_colornum += 1

    print("BEFORE THE COLOR REFINEMENT")
    print(get_coloring(D))
    print(get_coloring(I))
    print(get_coloring(disjoint_union.vertices))

    disjoint_union = partition_refinement_two(disjoint_union, len(disjoint_union.vertices))
    all_color_classes = get_color_classes(disjoint_union)
    print("\nAFTER THE COLOR REFINEMENT")
    print(get_coloring(D))
    print(get_coloring(I))
    print(get_coloring(disjoint_union.vertices))
    is_balanced_this = is_balanced_two(disjoint_union, all_color_classes)
    print("IS BALANCED: ", is_balanced_this)
    if not is_balanced_this:
        return 0
    if is_bijection(all_color_classes):
        return 1
    num = 0

    previous_coloring = get_previous_coloring(disjoint_union)

    for C in all_color_classes.values():
        if len(C.vertices) >= 4:
            x = C.vertices[0]
            for i in range(int(len(C.vertices) / 2), len(C.vertices)):
                num += count_isomorphism([x], [C.vertices[i]], disjoint_union,
                                         get_highest_colornum(all_color_classes) + 1, ka + 1)
                set_previous_coloring(disjoint_union, previous_coloring)
            break

    return num


def get_coloring(vertices):
    coloring = {}
    for v in vertices:
        if v.colornum not in coloring:
            coloring[v.colornum] = 1
        else:
            coloring[v.colornum] += 1
    return coloring


def get_color_classes(g):
    all_color_classes = {}
    for v in g.vertices:
        if v.colornum not in all_color_classes:
            all_color_classes[v.colornum] = ColorClass(v.colornum)
        all_color_classes[v.colornum].add_vertex(v)
    return all_color_classes


def is_bijection(color_classes):
    for color_class in color_classes.values():
        if len(color_class.vertices) != 2:
            return False

    return True


def get_highest_colornum(color_classes):
    highest_colornum = 0
    for color_class in color_classes.values():
        if color_class.colornum > highest_colornum:
            highest_colornum = color_class.colornum
    return highest_colornum


def is_balanced(graph):
    left = {}
    right = {}
    for vertex_count in range(0, len(graph.vertices)):
        if vertex_count <= len(graph.vertices) / 2 - 1:
            if graph.vertices[vertex_count].colornum not in left:
                left[graph.vertices[vertex_count].colornum] = 1
            else:
                left[graph.vertices[vertex_count].colornum] += 1
        else:
            if graph.vertices[vertex_count].colornum not in right:
                right[graph.vertices[vertex_count].colornum] = 1
            else:
                right[graph.vertices[vertex_count].colornum] += 1

    if right != left:
        return False
    return True


def is_balanced_two(graph, color_classes):
    left = 0
    right = 0
    for color_class in color_classes.values():
        for v in color_class.vertices:

            for i in range(len(graph.vertices)):
                if v == graph.vertices[i]:
                    if i <= (len(graph.vertices) / 2) - 1:
                        left += 1
                    else:
                        right += 1
                    break
        if left != right:
            return False

    return True


def list_of_colour_classes_bigger_eq_than_4(all_color_classes):
    temp = []
    for color_class in all_color_classes.values():
        if color_class.size() >= 4:
            temp.append(color_class)
    return temp


def get_previous_coloring(graph):
    previous_coloring = {}
    for vertex in graph.vertices:
        previous_coloring[vertex] = vertex.colornum
    return previous_coloring


def set_previous_coloring(graph, previous_coloring):
    for vertex in graph.vertices:
        vertex.colornum = previous_coloring[vertex]
