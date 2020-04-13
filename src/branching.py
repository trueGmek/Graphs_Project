from src.color_class import ColorClass
from src.color_refinement import *

'''
This function will be called when we got stable colorings, so I will not check that
'''


def test_branching():
    open_path_1 = os.path.relpath('../graphs/example_balanced_graph_1.gr', os.path.dirname(__file__))
    open_path_2 = os.path.relpath('../graphs/example_balanced_graph_1.gr', os.path.dirname(__file__))
    with open(open_path_1, 'r') as file:
        g = load_graph(file)
    with open(open_path_2, 'r') as file:
        h = load_graph(file)

    initialize_colornum(g)
    initialize_colornum(h)
    branching(g, h)


def branching(g, h):
    g, h = color_refinement(g), color_refinement(h)
    if not is_balanced(g, h):
        return 0
    if is_bijection(g, h):
        with open("graph_after_branching_g.dot", 'w') as file_stream:
            write_dot(g, file_stream)
        with open("graph_after_branching_h.dot", 'w') as file_stream:
            write_dot(h, file_stream)
        return 1

    num = 0
    index = 0

    g_color_classes = list_of_colour_classes_bigger_eq_than_k(get_color_classes(g), 2)
    # we select the first object from the list that has all the color classes that have size greater than two
    selected_color_class = g_color_classes[index]
    important_vertex_form_g = selected_color_class.vertices[0]  # select first vertex from first color class

    for vertex in get_color_class_form_h_that_is_equal_to_input_color_class(h, selected_color_class).vertices:
        previous_colornum = vertex.colornum
        important_vertex_form_g.colornum = get_highest_colornum(get_color_classes(g)) + 1
        vertex.colornum = important_vertex_form_g.colornum
        num += branching(g, h)
        vertex.colornum = previous_colornum

    print("Number of isomorphisms: ", num)

    return num


def get_color_class_form_h_that_is_equal_to_input_color_class(h, input_color_class):
    for color_class in get_color_classes(h).values():
        if (color_class.colornum == input_color_class.colornum
                and len(color_class.vertices) == len(input_color_class.vertices)):
            return color_class


def get_highest_colornum(list_of_color_classes):
    highest_colornum = -1
    for color_class in list_of_color_classes.values():
        if color_class.colornum > highest_colornum:
            highest_colornum = color_class.colornum
    return highest_colornum


def is_balanced(g, h):
    g_coloring, h_coloring = get_coloring(g), get_coloring(h)
    if g_coloring == h_coloring:
        return True
    else:
        return False


def is_bijection(g, h):
    g_coloring, h_coloring = get_coloring(g), get_coloring(h)
    if g_coloring != h_coloring:
        return False
    else:
        for key, value in g_coloring.items():
            if value != 1:
                return False
        return True


def get_color_classes(g):
    all_color_classes = {}
    for v in g.vertices:
        if v.colornum not in all_color_classes:
            all_color_classes[v.colornum] = ColorClass(v.colornum)
        all_color_classes[v.colornum].add_vertex(v)
    return all_color_classes


def list_of_colour_classes_bigger_eq_than_k(all_color_classes, k_size):
    temp = []
    for color_class in all_color_classes.values():
        if color_class.size() >= k_size:
            temp.append(color_class)
    return temp


def get_colour_class_list(g):
    coloring = {}
    for v in g.vertices:
        if v.colornum not in coloring:
            coloring[v.colornum] = []
        coloring[v.colornum].append(v)
    return coloring


def get_coloring(g):
    coloring = {}
    for v in g.vertices:
        if v.colornum not in coloring:
            coloring[v.colornum] = 1
        else:
            coloring[v.colornum] += 1
    return coloring
