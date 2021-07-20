import itertools
import functools
import util
import networkx as nx
from collections import deque
import random
from termcolor import cprint, colored
import multiprocessing
import time
from threading import Thread

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


def main():

    path1 = "kapitel2_src/1_Euler2.txt"
    path2 = "kapitel2_src/2_NormalerGraph.txt"
    path3 = "kapitel2_src/3_KreisGraph1.txt"
    path4 = "kapitel2_src/4_KreisGraph2.txt"
    path5 = "kapitel2_src/5_Planar1.txt"
    path6 = "kapitel2_src/6_Dijkstra10knoten.txt"
    path7 = "kapitel2_src/7_Graph_10K.txt"
    path8 = "kapitel2_src/weltkarte.txt"

    def test_graph(path):

        graph1 = util.build_graph(path, without_data=True)
        greedy_col(graph1,path) # Normaler Greedy_Coloring A, B, C, D, E
        # Thread(target=util.draw_graph_with_labels, args=(graph1),kwargs={'simple': True}).start()
        # util.draw_graph_with_labels(graph1,simple=True,save=True,path=path)
        
        graph1 = util.build_graph(path, without_data=True)
        for _ in range(100):
            greedy_col(graph1,path, randomize=True) # Randomized C, B, D A, E
        
        graph1 = util.build_graph(path, without_data=True)
        # opt_solution(graph1,path) # Brute Force
    
    # test_graph(path1)
    # test_graph(path2)
    # test_graph(path3)
    # test_graph(path4)
    # test_graph(path5)
    # test_graph(path6)
    # test_graph(path7)
    test_graph(path8)


@decorator
def greedy_col(graph,path, randomize=False):
    # util.draw_graph_with_labels(graph, simple=True)
    path = path.split('/')[len(path.split('/'))-1]

    if randomize:
        list_order = list(graph.nodes())
        random.shuffle(list_order)
    else:
        list_order = graph.nodes()

    max_color = greedy_col_inner(graph, list_order)

    graph_degree = get_max_degree(graph)[1]
    if randomize:
        cprint(f"Randomized GreedyColoring - {path}", "red")
        print_colored_line("green")
    else:
        cprint(f"Default GreedyColoring - {path}", "yellow")
        print_colored_line("green")
    print("Anzahl der Knoten\t", len(graph.nodes()), "\t V")
    print("Grad des Graphen:\t", graph_degree, "\t deg(G)")
    print("Obere Schranke:\t\t", (graph_degree + 1), "\t Delta G + 1")
    print("Benötigte Farben:\t", max_color, "\t cV(ui)")
    print()
    # print("Reihenfolge der Knoten:\t", list_order)


def greedy_col_inner(graph, list_order):
    for node in graph.nodes():
        graph.nodes[node]["color"] = "inf"

    max_color = 0
    for node in list_order:
        color_set = set()
        neighbors = list(graph.neighbors(node))
        neighbour_colors = [ # get colors of neighbor
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
def opt_solution(graph,path):

    path = path.split('/')[len(path.split('/'))-1]

    list_of_nodes = list(graph.nodes())
    permutations = list(itertools.permutations(list_of_nodes))
    partial_func = functools.partial(greedy_col_inner, graph)

    cprint(f"Optimale Lösung - {path}", "blue")
    print_colored_line("green")

    graph_degree = get_max_degree(graph)[1]
    print("Anzahl der Knoten\t", len(graph.nodes()), "\t V")
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


def calculate_time(

if __name__ == "__main__":
    main()