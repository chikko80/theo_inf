import networkx as nx
import matplotlib as plt
import pylab


class Node:
    def __init__(self, name, data):
        self.name = name
        self.data = data

class Edge:
    def __init__(self, first_node, second_node, weight):
        self.first_node = first_node
        self.second_node = second_node
        self.weight = weight

def main():

    graph = nx.Graph()
    node_list, edge_list = parser()

    for node in node_list:
        graph.add_node(node.name)

    for edge in edge_list:
        graph.add_edge(edge.first_node, edge.second_node, weight=edge.weight)

    draw_graph_with_labels(graph)

def draw_graph_with_labels(graph,simple=False):

    if simple:
        nx.draw(graph, with_labels=True)
        pylab.show()
    else:
        pos = nx.spring_layout(graph,seed=17)
        nx.draw(graph,pos, with_labels=True)
        edge_labels=dict([((u,v,),d['weight'])
        for u,v,d in graph.edges(data=True)])
        nx.draw_networkx_edge_labels(graph,pos,edge_labels=edge_labels)
        pylab.show()

def parser():

    with open("sources/Dijkstra.txt", mode="r", encoding="utf-8") as stream:
        lines = stream.readlines()
    

    node_list = []
    edge_list = []

    for line in lines:
        if line.startswith("knoten"):
            name = line.split(" ")[1]
            data = line.split(" ")[2]
            node_list.append(Node(name, data))
        elif line.startswith("kante"):
            first_node = line.split(" ")[1]
            second_node = line.split(" ")[2]
            weight = line.split(" ")[3]
            edge_list.append(Edge(first_node, second_node, weight))
        else:
            pass

    return node_list, edge_list


if __name__ == "__main__":
    main()