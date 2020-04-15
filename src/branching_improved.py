from src.color_class import ColorClass
from src.partition_refinement import *


def test_improved_branching():
    graphs = read_list_of_graphs_from_file('../graphs/branching/torus144.grl')
    disjoint_graph = graphs[5] + graphs[9]

    with open("color_refined_graph.dot_init", 'w') as file_stream:
        write_dot(disjoint_graph, file_stream)

    highest_colornum = 0

    disjoint_graph = partition_refinement(disjoint_graph, len(disjoint_graph.vertices))
    start = time.time()
    print(count_isomorphism([], [], disjoint_graph, get_highest_colornum(get_color_classes(disjoint_graph))))
    end = time.time()

    print("TIME: ", end - start)


def count_isomorphism(D, I, disjoint_union, highest_colornum):
    for i in range(len(D)):
        D[i].colornum = highest_colornum
        I[i].colornum = highest_colornum
        highest_colornum += 1

    disjoint_union = partition_refinement_two(disjoint_union, len(disjoint_union.vertices))

    all_color_classes = get_color_classes(disjoint_union)

    if not is_balanced(disjoint_union):
        return 0
    if is_bijection(disjoint_union):
        return 1
    num = 0

    previous_coloring = get_previous_coloring(disjoint_union)

    for C in list_of_colour_classes_bigger_eq_than_4(all_color_classes):
        x = C.vertices[0]
        for i in range(int(len(C.vertices) / 2), len(C.vertices)):
            num += count_isomorphism([x], [C.vertices[i]], disjoint_union,
                                     get_highest_colornum(all_color_classes) + 1)
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


def is_bijection(graph):
    left_graph = graph.vertices[:int(len(graph.vertices) / 2)]
    right_graph = graph.vertices[-int(len(graph.vertices) / 2):]
    left_coloring, right_coloring = get_coloring(left_graph), get_coloring(right_graph)
    if left_coloring != right_coloring:
        return False
    else:
        for key, value in left_coloring.items():
            if value != 1:
                return False
        return True


def get_highest_colornum(color_classes):
    highest_colornum = 0
    for color_class in color_classes.values():
        if color_class.colornum > highest_colornum:
            highest_colornum = color_class.colornum
    return highest_colornum


def is_balanced(graph):
    left_graph = graph.vertices[:int(len(graph.vertices) / 2)]
    right_graph = graph.vertices[-int(len(graph.vertices) / 2):]
    g_coloring, h_coloring = get_coloring(left_graph), get_coloring(right_graph)
    if g_coloring == h_coloring:
        return True
    else:
        return False


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


def read_list_of_graphs_from_file(path):
    open_path = os.path.relpath(path, os.path.dirname(__file__))
    with open(open_path, 'r') as file:
        problematic_file = load_graph(file, Graph, True)

    return problematic_file[0]
