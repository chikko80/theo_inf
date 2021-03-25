import util
import networkx as nx


def main():
    path1 = "sources/Dijkstra.txt"

    graph = nx.Graph()
    node_list, edge_list = util.parser(path1)

    for node in node_list:

        graph.add_node(node.name)

    for edge in edge_list:
        graph.add_edge(edge.first_node, edge.second_node, weight=edge.weight)

    util.draw_graph_with_labels(graph)



if __name__ == "__main__":
    main()