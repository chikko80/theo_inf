import util
import networkx as nx
from collections import deque

# http://discrete.openmathbooks.org/dmoi2/sec_paths.html#:~:text=A%20graph%20has%20an%20Euler%20circuit%20if%20and%20only%20if,two%20vertices%20with%20odd%20degree.


def main():

    path1 = "sources/Fluss.txt"
    path2 = "sources/Fluss2.txt"

    graph2 = util.build_graph(path1, flow_network=True)

    four_a(graph2)


def four_a(graph):
    print(list(nx.dfs_edges(graph, "S")))
    util.draw_graph_with_labels(graph, simple=False, flow_network=True)


if __name__ == "__main__":
    main()