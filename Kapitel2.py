import itertools
import functools
import util
import networkx as nx
from collections import deque
import random
from termcolor import cprint, colored
import multiprocessing
import time

# http://discrete.openmathbooks.org/dmoi2/sec_paths.html#:~:text=A%20graph%20has%20an%20Euler%20circuit%20if%20and%20only%20if,two%20vertices%20with%20odd%20degree.


def decorator(func):
    def inner(*args, **kwargs):
        print("\n")
        print_colored_line("green")
        func(*args, **kwargs)
        print_colored_line("green")

    return inner


def print_colored_line(color):
    cprint( "---------------------------------------------------------------------------------------------", color)


def print_header(message, color):
    cprint( "---------------------------------------------------------------------------------------------", color)
    cprint(message, color)
    cprint( "---------------------------------------------------------------------------------------------", color)


def main():

    path1 = "sources/Euler2.txt"
    path2 = "sources/Dijkstra10knoten.txt"

    graph1 = util.build_graph(path1, without_data=True)
    greedy_col(graph1)
    graph1 = util.build_graph(path1, without_data=True)
    greedy_col(graph1, randomize=True)
    graph1 = util.build_graph(path1, without_data=True)
    opt_solution(graph1)

    graph2 = util.build_graph(path2, without_data=False)
    greedy_col(graph2)
    graph2 = util.build_graph(path2, without_data=False)
    greedy_col(graph2, randomize=True)
    graph2 = util.build_graph(path2, without_data=False)
    opt_solution(graph2)


@decorator
def greedy_col(graph, randomize=False):
    # util.draw_graph_with_labels(graph, simple=True)

    if randomize:
        list_order = list(graph.nodes())
        random.shuffle(list_order)
    else:
        list_order = graph.nodes()

    max_color = greedy_col_inner(graph, list_order)

    graph_degree = get_max_degree(graph)[1]
    if randomize:
        cprint("Randomized GreedyColoring", "red")
        print_colored_line("green")
    else:
        cprint("Default GreedyColoring", "yellow")
        print_colored_line("green")
    print("Grad des Graphen:\t", graph_degree, "\t deg(G)")
    print("Obere Schranke:\t\t", (graph_degree + 1), "\t Delta G + 1")
    print("Benötigte Farben:\t", max_color, "\t cV(ui)")
    print()
    print("Reihenfolge der Knoten:\t", list_order)


def greedy_col_inner(graph, list_order):
    for node in graph.nodes():
        graph.nodes[node]["color"] = "inf"

    max_color = 0
    for node in list_order:
        color_set = set()
        neighbors = list(graph.neighbors(node))
        neighbour_colors = [
            graph.nodes[node]["color"]
            for node in graph.neighbors(node)
            if graph.nodes[node]["color"] and graph.nodes[node]["color"] != "inf"
        ]
        smallest_free_color = get_smallest_free_color(graph, neighbour_colors)
        graph.nodes[node]["color"] = smallest_free_color

        if max_color < smallest_free_color:
            max_color = smallest_free_color
    return max_color


@decorator
def opt_solution(graph):
    list_of_nodes = list(graph.nodes())
    permutations = list(itertools.permutations(list_of_nodes))
    partial_func = functools.partial(greedy_col_inner, graph)

    cprint("Optimale Lösung", "blue")
    print_colored_line("green")

    graph_degree = get_max_degree(graph)[1]
    print("Grad des Graphen:\t", graph_degree, "\t deg(G)")
    print("Obere Schranke:\t\t", (graph_degree + 1), "\t Delta G + 1")
    print()
    print("Mögliche Kombinationen:\t", len(permutations))

    start = time.time()
    with multiprocessing.Pool() as pool:  # default is optimal number of processes
        results = pool.map(partial_func, permutations)
    req_time = time.time() - start
    print("Set der Ergebnisse:\t", set(results), f"\t Berechnet in {req_time} Sekunden")


def get_max_degree(graph):
    degrees = [(node, val) for (node, val) in graph.degree()]
    degrees.sort(key=lambda x: x[1])
    degrees.reverse()
    return degrees[0]  # returning tuple ('A',3)


def get_smallest_free_color(graph, neighbors_colors):
    max_degree = get_max_degree(graph)[1]
    higher_bound = max_degree + 1
    for i in range(1, max_degree + 1):
        if i not in neighbors_colors:
            return i


if __name__ == "__main__":
    main()