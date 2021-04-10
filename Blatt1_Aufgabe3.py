import util
import networkx as nx
from collections import deque

# http://discrete.openmathbooks.org/dmoi2/sec_paths.html#:~:text=A%20graph%20has%20an%20Euler%20circuit%20if%20and%20only%20if,two%20vertices%20with%20odd%20degree.


def main():

    path1 = "sources/Dijkstra.txt"

    graph1 = util.build_graph(path1, without_data=False)

    def test_dijkstra(graph, source, dest):
        print("Libary Length: ", nx.dijkstra_path_length(graph, source, dest))
        print("Libary Path: ", nx.dijkstra_path(graph, source, dest))
        print("Our Implementation: ", three_a(graph, source, dest))

    # test_dijkstra(graph1, "A", "D")
    # test_dijkstra(graph1, "H", "B")
    three_b(graph1)


def three_a(graph, origin, destination):
    """"""
    # util.draw_graph_with_labels(graph, simple=True)
    return shortest_path(graph, origin, destination)


def three_b(graph):
    """
    defintion of circuit: closed trial with visited edges >= 3

    """
    kruskal(graph)


def kruskal(graph):
    weight_dict = {}
    for edge in graph.edges:
        weight_dict[edge] = graph.get_edge_data(*edge)["weight"]

    sorted_weight_dict = dict(sorted(weight_dict.items(), key=lambda item: item[1]))

    min_span = nx.Graph()
    for node in list(min_span.nodes):
        min_span.add_node(node.name)

    for edge, weight in sorted_weight_dict.items():
        min_span.add_edge(*edge, weight=weight)
        try:
            if nx.find_cycle(min_span):
                min_span.remove_edge(*edge)
        except nx.exception.NetworkXNoCycle:
            pass
    util.draw_graph_with_labels(min_span, simple=False)


def shortest_path(graph, origin, destination):
    visited, paths = dijkstra(graph, origin)
    full_path = deque()
    _destination = paths[destination]

    while _destination != origin:
        full_path.appendleft(_destination)
        _destination = paths[_destination]

    full_path.appendleft(origin)
    full_path.append(destination)

    return visited[destination], list(full_path)


def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node

        if min_node is None:
            break

        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges(min_node):
            edge = edge[1]
            weight = current_weight + int(graph.get_edge_data(min_node, edge)["weight"])
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = min_node

    return visited, path


if __name__ == "__main__":
    main()