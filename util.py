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

def parser(path,without_data=False):

    with open(path, mode="r", encoding="utf-8") as stream:
        lines = stream.readlines()

    node_list = []
    edge_list = []

    for line in lines:
        if line.startswith("knoten"):
            name = line.split(" ")[1].strip()
            if without_data:
                node_list.append(Node(name, None))
            else:
                data = line.split(" ")[2].strip()
                node_list.append(Node(name, data))

        elif line.startswith("kante"):
            first_node = line.split(" ")[1].strip()
            second_node = line.split(" ")[2].strip()
            if without_data:
                edge_list.append(Edge(first_node, second_node, None))
            else:
                weight = line.split(" ")[3].strip()
                edge_list.append(Edge(first_node, second_node, weight))
        else:
            pass

    return node_list, edge_list