import util
import networkx as nx

# http://discrete.openmathbooks.org/dmoi2/sec_paths.html#:~:text=A%20graph%20has%20an%20Euler%20circuit%20if%20and%20only%20if,two%20vertices%20with%20odd%20degree.


def main():

    path1 = "sources/Euler1.txt"
    path2 = "sources/Euler2.txt"
    path3 = "sources/Dijkstra.txt"
    path4 = "sources/sicher_kein_kreis.txt"

    graph2 = util.build_graph(path2)

    two_a(graph2)
    two_b(graph2)
    two_c(graph2)



def two_a(graph):
    """
    if all the vertices of a graph have even degree,
    then the graph has an Euler circuit,
    and if there are exactly two vertices with odd degree,
        the graph has an Euler path.
    """

    util.draw_graph_with_labels(graph, simple=True)

    # gibt uns degree für jeden knoten in liste als tuple
    degrees = graph.degree()
    print(degrees)
    print("2a) Have Euler Circuit: ", have_euler_circuit(degrees))
    print("2a) Have Euler Path: ", have_euler_path(degrees))


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


def two_b(graph):
    """
    defintion of circuit: closed trial with visited edges >= 3
    """

    # util.draw_graph_with_labels(graph, simple=True)
    dfs_result = list(nx.dfs_edges(graph,source='A'))
    print('2b) ', dfs_result)

    util.draw_graph_with_labels(nx.dfs_tree(graph,source="A"), simple=True)



def two_c(graph):
    """
    defintion of circuit: closed trial with visited edges >= 3
    """

        # util.draw_graph_with_labels(graph, simple=True)

    print('2c) Hat Zyklus: ', isCyclic(graph)) # eigener algorithmus true oder false
    try:
        print('2c) nEin möglicher Kreis: ' , nx.find_cycle(graph)) # findet einen kreis
    except:
        print('2c) nkein kreis gefunden')
    print('2c) nAlle möglichen Pfade: ', nx.cycle_basis(graph)) # findet alle kreise



def isCyclicRecursive(graph,node, visited, parent):

    visited.append(node) # Makiere aktuellen knoten als besucht
    for neighbor_node in graph.neighbors(node): # schaue von aktuellem knoten alle nachbarn an

        if neighbor_node not in visited: # wenn der nachbar noch nicht besucht rufe funktion wieder auf
            if isCyclicRecursive(graph,neighbor_node, visited, node): # mit nachbar knoten und der aktuellen als parent
                return True
        # wenn visited aber nicht parent 
        elif parent != neighbor_node: # wenn der knoten schon besucht ist aber der nach nachbar nicht der aktuelle parent ist haben wir einen kreis
            return True

    return False

# Returns true if the graph
# contains a cycle, else false.
def isCyclic(graph):

    visited = [] 
    for node in graph.nodes(): # Schaue alle knoten an
        if node not in visited: # wenn der knoten nicht besucht wurde, rufe recursive neue funktion auf
            if (isCyclicRecursive(graph,node, visited, -1)) == True: # übergebe graph, aktuellen knoten, und visted
                return True

    return False


if __name__ == "__main__":
    main()