from src.color_refinement import *
from src.color_class import ColorClass

'''
This function will be called when we got stable colorings, so I will not check that
'''


def test_branching():
    open_path = os.path.relpath('../graphs/example_balanced_graph_1.gr', os.path.dirname(__file__))
    with open(open_path, 'r') as file:
        g = load_graph(file)
    g = color_refinement(g)
    h = g
    print("GRAPH g = h:")
    print(g)
    print("color list:\n", str(get_coloring(g)))
    print("Is balanced: ", str(is_balanced(g, h)))
    print("Is g bijection of h: ", str(is_bijection(g, h)))
    list_of_colour_classes_bigger_eg_than_k(get_color_classes(g), 11)


def branching(g, h):
    g, h = color_refinement(g), color_refinement(h)
    colour_class_list = get_colour_class_list(g)
    index_of_color_class = 0  # index of color class that has more than two members in one graph
    first_vertex_from_color_class = None
    highest_color = 0
    if not is_balanced(g, h):
        return 0
    if is_bijection(g, h):
        return 1
    num = 0

    print(get_coloring(g))

    for key, value in get_coloring(g).items():
        if key > highest_color:
            highest_color = key
        if value >= key + 2:
            index_of_color_class = key
            first_vertex_from_color_class = colour_class_list[index_of_color_class][0]
            first_vertex_from_color_class.colornum = highest_color + 1
            break

        for vertex in g.vertices:
            if vertex.label == first_vertex_from_color_class.label:
                vertex.colornum = first_vertex_from_color_class.colornum

    for vertex in get_colour_class_list(h)[index_of_color_class]:
        for v in h.vertices:
            if v.label == vertex.label:
                v.colornum = highest_color
        num += branching(g, h)

    print("Number of ", "I S O M O R P H I S M S", num, " K U R W A")
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


def get_color_classes(g):
    all_color_classes = {}
    for v in g.vertices:
        if v.colornum not in all_color_classes:
            all_color_classes[v.colornum] = ColorClass(v.colornum)
        all_color_classes[v.colornum].add_vertex(v)
    return all_color_classes


def list_of_colour_classes_bigger_eg_than_k(all_color_classes, k_size):
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
            coloring[v.colornum] = v.colornum
        else:
            coloring[v.colornum] += 1
    return coloring
