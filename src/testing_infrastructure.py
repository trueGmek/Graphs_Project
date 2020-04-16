import os
from time import time

from src.branching import count_isomorphism, set_up_colornum
from src.graph import Graph
from src.graph_io import load_graph
from src.partition_refinement import partition_refinement

FILE_NAME_GI = '../graphs/basicGI3.grl'
FILE_NAME_AUTO = '../graphs/basicAut2.gr'
FILE_NAME_ISO = '../graphs/basicGIAut.grl'


def do_the_tests():
    print_the_welcome_message()
    x = input()
    tf = 0
    if x == '0':
        print("Sets of isomorphic graphs:")
        graphs = read_list_of_graphs_from_file(FILE_NAME_GI)
        n = len(graphs)
        previous_checks = []
        for i in range(n):
            if i in previous_checks:
                continue
            isomorphic_graphs = [i]
            for j in range(i + 1, n):
                t1 = time()
                disjoint_graph = graphs[i] + graphs[j]
                highest_colornum = set_up_colornum(disjoint_graph)
                if count_isomorphism([], [], disjoint_graph, highest_colornum) > 1:
                    isomorphic_graphs.append(j)
                    previous_checks.append(j)
                t2 = time()
                tf += (t2 - t1)
            previous_checks.append(i)
            print(str(isomorphic_graphs))
        print("Time of computation [s]: {}".format(tf))

    if x == '1':
        print("Graph: Number of automorphisms:")
        graphs = read_list_of_graphs_from_file(FILE_NAME_AUTO)
        g_counter = 0

        t1 = time()
        for g in graphs:
            disjoint_graph = g + g
            highest_colornum = set_up_colornum(disjoint_graph)
            print(g_counter, ":  ",
                  count_isomorphism([], [], disjoint_graph, highest_colornum))
            g_counter += 1
        t2 = time()
        print("Time of computation [s]: {}".format(t2 - t1))

    if x == '2':
        print("Sets of isomorphic graphs: Number of automorphisms: ")
        graphs = read_list_of_graphs_from_file(FILE_NAME_ISO)
        n = len(graphs)
        list_of_sets = []

        for i in range(n):
            for j in range(i + 1, n):
                t1 = time()
                disjoint_graph = graphs[i] + graphs[j]
                highest_colornum = set_up_colornum(disjoint_graph)
                disjoint_graph = partition_refinement(disjoint_graph, len(disjoint_graph))
                number_of_isomorphisms = count_isomorphism([], [], disjoint_graph, highest_colornum)
                if number_of_isomorphisms > 1:
                    print('[', i, j, "]     ", number_of_isomorphisms)
                    list_of_sets.append(i)
                    list_of_sets.append(j)
                t2 = time()
                tf += (t2 - t1)

        print("Graph: Number of automorphisms:")
        g_counter = 0
        for g in graphs:
            t1 = time()
            if g_counter not in list_of_sets:
                disjoint_graph = g + g
                highest_colornum = set_up_colornum(disjoint_graph)
                print('[', g_counter, "]\t\t",
                      count_isomorphism([], [], disjoint_graph, highest_colornum))
            g_counter += 1
            t2 = time()
            tf += (t2 - t1)
        print("Time of computation [s]: {}".format(tf))


def read_list_of_graphs_from_file(path):
    open_path = os.path.relpath(path, os.path.dirname(__file__))
    with open(open_path, 'r') as file:
        problematic_file = load_graph(file, Graph, True)

    return problematic_file[0]


def print_the_welcome_message():
    print("For GI select: 0\n"
          "For # of Automorphisms: 1\n"
          "For # Isomorphism between two graphs: 2")
