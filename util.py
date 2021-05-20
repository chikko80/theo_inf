import networkx as nx
from matplotlib import pyplot as plt
import pylab


class Node:
    def __init__(self, name, data):
        self.name = name
        self.data = data


class Edge:
    def __init__(self, first_node, second_node, weight, flow=None, capacity=None):
        self.first_node = first_node
        self.second_node = second_node
        self.weight = int(weight) if weight else None
        self.flow = int(flow) if type(flow) == int else None
        self.capacity = int(capacity) if capacity else None


def draw_graph_with_labels(graph, simple=False, save=False,path=None, flow_network=False):
    if simple and save and path:
        nx.draw(graph, with_labels=True)
        file_name = path.split('/')[len(path.split('/'))-1].replace('.txt','.png')
        plt.savefig(f'img/{file_name}')
        plt.clf()

    elif simple:
        nx.draw(graph, with_labels=True)
        pylab.show()
    else:

        pos = nx.spring_layout(graph, seed=17)
        nx.draw(graph, pos, with_labels=True)
        edge_labels = dict( [ ( ( u, v,), d["capacity"],) for u, v, d in graph.edges(data=True) ])
        nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)
        pylab.show(block)


def parser(path, without_data, flow_network):

    with open(path, mode="r", encoding="utf-8") as stream:
        lines = stream.readlines()

    node_list = []
    edge_list = []

    for line in lines:
        if line.startswith("knoten"):
            name = line.split(" ")[1].strip()
            node_list.append(Node(name, None))

        elif line.startswith("kante"):
            first_node = line.split(" ")[1].strip()
            second_node = line.split(" ")[2].strip()
            if without_data:
                edge_list.append(Edge(first_node, second_node, None))
            elif flow_network:
                weight = line.split(" ")[3].strip()
                edge_list.append(
                    Edge(first_node, second_node, None, flow=0, capacity=weight)
                )
            else:
                weight = line.split(" ")[3].strip()
                edge_list.append(Edge(first_node, second_node, weight))
        else:
            pass
    return node_list, edge_list


def build_graph(path, without_data=True, flow_network=False):
    if flow_network:
        graph = nx.DiGraph()
    else:
        graph = nx.Graph()
    node_list, edge_list = parser(path, without_data, flow_network)

    for node in node_list:
        graph.add_node(node.name)

    for edge in edge_list:
        if flow_network:
            graph.add_edge( edge.first_node, edge.second_node, flow=edge.flow, capacity=edge.capacity)
        else:
            graph.add_edge(edge.first_node, edge.second_node, weight=edge.weight)
    return graph