import util
import networkx as nx
from collections import deque
from networkx.algorithms.traversal import depth_first_search

# http://discrete.openmathbooks.org/dmoi2/sec_paths.html#:~:text=A%20graph%20has%20an%20Euler%20circuit%20if%20and%20only%20if,two%20vertices%20with%20odd%20degree.


def main():

    path1 = "sources/Fluss.txt"
    path2 = "sources/Fluss2.txt"
    path3 = "sources/Euler2.txt"

    graph1 = util.build_graph(path1, flow_network=True)
    graph2 = util.build_graph(path2, flow_network=True)
    graph3 = util.build_graph(path3, without_data=True)

    # four_a(graph1)
    four_a(graph2)
    # four_a(graph3)


def four_a(graph):
    # print(list(nx.dfs_edges(graph, source="S")))
    # dfs(graph)
    from networkx.algorithms.flow import shortest_augmenting_path

    util.draw_graph_with_labels(graph, simple=True)
    print(nx.maximum_flow(graph, "S", "T"))


def dfs_rec(graph, node, visited, parent):

    visited.append(node)
    for neighbor_node in graph.neighbors(node):
        if neighbor_node not in visited:
            dfs_rec(graph, neighbor_node, visited, node)


# Returns true if the graph
# contains a cycle, else false.
def dfs(graph):

    visited = []
    graph_nodes = set_source_at_first(list(graph.nodes()), "S")
    for node in graph_nodes:
        if node not in visited:
            dfs_rec(graph, node, visited, -1)
    print(visited)


def set_source_at_first(graph_nodes: list, source):
    graph_nodes.remove(source)
    graph_nodes.insert(0, source)
    return graph_nodes


if __name__ == "__main__":
    main()