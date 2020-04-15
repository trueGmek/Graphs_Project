import os
import time

from src.graph_io import *


def second_coloring(G):
    all_numbers = []
    extra_partition = 0

    for v in G.vertices:
        if v.colornum not in all_numbers:
            all_numbers.append(v.colornum)

    if 0 in all_numbers:
        extra_partition = 1
        all_numbers.remove(0)

    return all_numbers, extra_partition


def initial_coloring(G):
    for v in G.vertices:
        v.colornum = v.degree

    all_numbers = []
    extra_partition = 0

    for v in G.vertices:
        if v.colornum not in all_numbers:
            all_numbers.append(v.colornum)

    if 0 in all_numbers:
        extra_partition = 1
        all_numbers.remove(0)

    return all_numbers, extra_partition


def generate_n_primes(N):
    primes = []
    chkthis = 2
    while len(primes) < N:
        ptest = [chkthis for i in primes if chkthis % i == 0]
        primes += [] if ptest else [chkthis]
        chkthis += 1
    return primes


def count_vertices(color, G):
    i = 0
    for v in G.vertices:
        if v.colornum == color:
            i = i + 1
        if i > 1:
            return True
    return False


def change_colornum(list_prime, all_numbers, temp_list, G):
    start = 0
    for num in all_numbers:
        prime = list_prime[start]
        for v in G.vertices:
            if v.degree >= 1 and v.colornum == num:
                for w in v.neighbours:
                    temp_list[v.label] += (prime ** w.colornum)

        start += 1
    # print(temp_list)

    for v in G.vertices:
        if temp_list[v.label] != 0:
            v.colornum = temp_list[v.label]


def partition_refinement(G, n):
    x = 0

    list_prime = generate_n_primes(n)
    temp_list = [0] * n
    all_numbers, extra_partition = initial_coloring(G)

    change_colornum(list_prime, all_numbers, temp_list, G)

    prev_all_numbers = all_numbers

    all_numbers = []
    temp_list = [0] * n

    for v in G.vertices:
        if v.colornum not in all_numbers:
            all_numbers.append(v.colornum)

    if 0 in all_numbers:
        all_numbers.remove(0)

    a = 1

    for i in range(len(all_numbers)):
        for v in G.vertices:
            if v.colornum == all_numbers[i]:
                temp_list[v.label] = a
        a = a + 1

    for v in G.vertices:
        if temp_list[v.label] != 0:
            v.colornum = temp_list[v.label]

    all_numbers = []
    temp_list = [0] * n

    for v in G.vertices:
        if v.colornum not in all_numbers:
            all_numbers.append(v.colornum)

    if 0 in all_numbers:
        all_numbers.remove(0)

    # print(allnumbers)
    # print(prev_all_numbers)

    # x += 1

    while len(all_numbers) != len(prev_all_numbers):
        change_colornum(list_prime, all_numbers, temp_list, G)

        prev_all_numbers = all_numbers

        all_numbers = []
        temp_list = [0] * n

        for v in G.vertices:
            if v.colornum not in all_numbers:
                all_numbers.append(v.colornum)

        if 0 in all_numbers:
            all_numbers.remove(0)

        # print(all_numbers)

        a = 1
        for i in range(len(all_numbers)):
            for v in G.vertices:
                if v.colornum == all_numbers[i]:
                    temp_list[v.label] = a
            a = a + 1

        for v in G.vertices:
            if temp_list[v.label] != 0:
                v.colornum = temp_list[v.label]

        all_numbers = []
        temp_list = [0] * n

        for v in G.vertices:
            if v.colornum not in all_numbers:
                all_numbers.append(v.colornum)
        if 0 in all_numbers:
            all_numbers.remove(0)

        # x += 1
    if extra_partition == 1:
        partitions = len(all_numbers) + 1
    else:
        partitions = len(all_numbers)

    # print(x)

    # print("Number of partitions:")
    # print(partitions)
    # print("Number of vertices:")
    # print(n)

    if partitions != n:
        # print("Isomorphism can't be said by Color Refinement only.")
        pass

    return G


# if __name__ == "__main__":
#     start_time = time.time()
#
#     cur_path = os.path.dirname(__file__)
#     new_path = os.path.relpath('../graphs/branching/lecture_graphs.grl', cur_path)
#
#     with open(new_path, 'r') as file_stream:
#         graph_list = load_graph(file_stream, read_list=True)[0]
#         G = Graph(False)
#         G = G + graph_list[0]
#         G = G + graph_list[1]
#         n = len(G.vertices)
#
#     output_graph = partition_refinement(G, n)
#
#     with open("color_refined_graph.dot", 'w') as file_stream:
#         write_dot(output_graph, file_stream)
#
#     print("--- %s seconds ---" % (time.time() - start_time))
#
# with open("color_refined_graph_newCode.dot", 'w') as g:
#     write_dot(G, g)

def partition_refinement_two(G, n):
    x = 0

    list_prime = generate_n_primes(n)
    temp_list = [0] * n
    all_numbers, extra_partition = second_coloring(G)

    change_colornum(list_prime, all_numbers, temp_list, G)

    prev_all_numbers = all_numbers

    all_numbers = []
    temp_list = [0] * n

    for v in G.vertices:
        if v.colornum not in all_numbers:
            all_numbers.append(v.colornum)

    if 0 in all_numbers:
        all_numbers.remove(0)

    a = 1

    for i in range(len(all_numbers)):
        for v in G.vertices:
            if v.colornum == all_numbers[i]:
                temp_list[v.label] = a
        a = a + 1

    for v in G.vertices:
        if temp_list[v.label] != 0:
            v.colornum = temp_list[v.label]

    all_numbers = []
    temp_list = [0] * n

    for v in G.vertices:
        if v.colornum not in all_numbers:
            all_numbers.append(v.colornum)

    if 0 in all_numbers:
        all_numbers.remove(0)

    # print(all_numbers)
    # print(prev_all_numbers)

    # x += 1

    while len(all_numbers) != len(prev_all_numbers):
        change_colornum(list_prime, all_numbers, temp_list, G)

        prev_all_numbers = all_numbers

        all_numbers = []
        temp_list = [0] * n

        for v in G.vertices:
            if v.colornum not in all_numbers:
                all_numbers.append(v.colornum)

        if 0 in all_numbers:
            all_numbers.remove(0)

        # print(all_numbers)

        a = 1
        for i in range(len(all_numbers)):
            for v in G.vertices:
                if v.colornum == all_numbers[i]:
                    temp_list[v.label] = a
            a = a + 1

        for v in G.vertices:
            if temp_list[v.label] != 0:
                v.colornum = temp_list[v.label]

        all_numbers = []
        temp_list = [0] * n

        for v in G.vertices:
            if v.colornum not in all_numbers:
                all_numbers.append(v.colornum)
        if 0 in all_numbers:
            all_numbers.remove(0)

        # x += 1
    if extra_partition == 1:
        partitions = len(all_numbers) + 1
    else:
        partitions = len(all_numbers)

    # print(x)

    # print("Number of partitions:")
    # print(partitions)
    # print("Number of vertices:")
    # print(n)

    if partitions != n:
        # print("Isomorphism can't be said by Color Refinement only.")
        pass

    return G
