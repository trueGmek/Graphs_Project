from src.color_refinement import *

'''
This function will be called when we got stable colorings, so I will not check that
'''


def test_branching():
    open_path = os.path.relpath('../graphs/examplegraph.gr', os.path.dirname(__file__))
    with open(open_path, 'r') as file:
        g = load_graph(file)
    g = color_refinement(g)
    h = g
    print(g)
    print(h)
    print(is_balanced(g, h))
    print(is_bijection(g, h))
    branching(g, h)


def branching(g, h):
    g, h = color_refinement(g), color_refinement(h)
    colour_class_list = get_colour_class_list(g)
    index_of_color_class = 0  # index of color class that has more than two members in one graph
    first_vertex_from_color_class = None
    highest_color = 0
    if is_balanced(g, h):
        return 0
    if is_bijection(g, h):
        return 1
    num = 0

    for key, value in get_coloring(g):
        if key > highest_color:
            highest_color = key
        if value >= key + 2:
            index_of_color_class = value
            first_vertex_from_color_class = colour_class_list[index_of_color_class][0]
            first_vertex_from_color_class.colornum = highest_color
            break

        for vertex in g.vertices:
            if vertex.label == first_vertex_from_color_class.label:
                vertex.colornum = first_vertex_from_color_class.colornum

    for vertex in get_colour_class_list(h)[index_of_color_class]:
        for v in h.vertices:
            if v.label == vertex.label:
                v.colornum = highest_color
        num += branching(g, h)
    return num


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
            if key != value:
                return False
        return True


def get_colour_class_list(g):
    coloring = {}
    for v in g.vertices:
        if v.colornum not in coloring:
            coloring[v.colornum] = []
        coloring[v.colornum].append(v)
    return coloring
