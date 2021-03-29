import util
import networkx as nx

# http://discrete.openmathbooks.org/dmoi2/sec_paths.html#:~:text=A%20graph%20has%20an%20Euler%20circuit%20if%20and%20only%20if,two%20vertices%20with%20odd%20degree.


def main():

    # two_a()
    two_b()
    # two_c()


def have_euler_circuit(degrees):
    for degree in degrees:
        if degree[1] % 2 != 0:
            return False
    return True


def have_euler_path(degrees):
    odd_degrees = 0
    for degree in degrees:
        if odd_degrees > 2:
            return False
        if degree[1] % 2 != 0:
            odd_degrees += 1

    if odd_degrees == 2:
        return True
    return False


def two_a():
    """
    if all the vertices of a graph have even degree,
    then the graph has an Euler circuit,
    and if there are exactly two vertices with odd degree,
        the graph has an Euler path.
    """
    euler1 = "sources/Euler1.txt"
    euler2 = "sources/Euler2.txt"

    def check_euler(path):
        graph = nx.Graph()
        node_list, edge_list = util.parser(path, without_data=True)

        for node in node_list:
            graph.add_node(node.name)

        for edge in edge_list:
            graph.add_edge(edge.first_node, edge.second_node, weight=edge.weight)

        util.draw_graph_with_labels(graph, simple=True)

        # gibt uns degree für jeden knoten in liste als tuple
        degrees = graph.degree()
        print(degrees)
        print("Have Euler Circuit: ", have_euler_circuit(degrees))
        print("Have Euler Path: ", have_euler_path(degrees))

    check_euler(euler1)
    check_euler(euler2)


def two_b():
    """
    defintion of circuit: closed trial with visited edges >= 3
    """
    graph1 = "sources/Euler1.txt"
    graph2 = "sources/Euler2.txt"
    graph2 = "sources/Dijkstra.txt"

    def print_dfs(path):
        graph = nx.Graph()
        node_list, edge_list = util.parser(path, without_data=True)

        for node in node_list:
            graph.add_node(node.name)

        for edge in edge_list:
            graph.add_edge(edge.first_node, edge.second_node, weight=edge.weight)

        # util.draw_graph_with_labels(graph, simple=True)
        dfs_result = list(nx.dfs_edges(graph,source='A'))
        print(dfs_result)

        util.draw_graph_with_labels(nx.dfs_tree(graph,source="A"), simple=True)

    print_dfs(graph1)



def two_c():
    """
    defintion of circuit: closed trial with visited edges >= 3
    """
    graph1 = "sources/Euler1.txt"
    graph2 = "sources/Euler2.txt"
    graph3 = "sources/Dijkstra.txt"
    graph4 = "sources/sicher_kein_kreis.txt"

    graph_list = [graph1,graph2,graph3,graph4]

    def print_cycles(path):
        graph = nx.Graph()
        node_list, edge_list = util.parser(path, without_data=True)

        for node in node_list:
            graph.add_node(node.name)

        for edge in edge_list:
            graph.add_edge(edge.first_node, edge.second_node, weight=edge.weight)

        # util.draw_graph_with_labels(graph, simple=True)

        print(isCyclic(graph)) # eigener algorithmus true oder false
        try:
            print(nx.find_cycle(graph)) # findet einen kreis
        except:
            print('kein kreis gefunden')
        print(nx.cycle_basis(graph)) # findet alle kreise

    for graph in graph_list:
        print(graph)
        print_cycles(graph)
        print()


def isCyclicUtil(graph,node, visited, parent):

    # Mark the current node as visited
    visited.append(node)

    for neighbor_node in graph.neighbors(node):

        if neighbor_node not in visited:
            if isCyclicUtil(graph,neighbor_node, visited, node):
                return True
        # wenn visited aber nicht parent 
        elif parent != neighbor_node:
            return True

    return False

# Returns true if the graph
# contains a cycle, else false.
def isCyclic(graph):

    visited = [] 
    for node in graph.nodes():
        if node not in visited:
            if (isCyclicUtil(graph,node, visited, -1)) == True:
                return True

    return False


if __name__ == "__main__":
    main()