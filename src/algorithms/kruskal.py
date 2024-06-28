
# Find a minimum spanning tree of a weighted undirected graph, using kruskal's algorithm
# Kruskal's algorithm uses a dijoint set data structure to add new edges to the minimum
# spanning tree only if they are cut, meaning only if they are in different trees, thus
# using the disjoint data structure on;y if they are in different sets


import networkx as nx
import matplotlib.pyplot as plt

# Graph Utils


def add_vertex(Adj, Name, Idx, u_name):
    if u_name in Idx:
        u = Idx[u_name]
    else:
        u = len(Adj)
        Adj.append([])
        Name.append(u_name)
        Idx[u_name] = u

    return u


def read_undirected_graph_weights(filename):
    f = open(filename)
    Name = []
    Idx = {}
    Adj = []

    for l in f:
        u_name, v_name, c = l.strip().split()
        c = float(c)
        u = add_vertex(Adj, Name, Idx, u_name)
        v = add_vertex(Adj, Name, Idx, v_name)

        Adj[u].append((v, c))
        Adj[v].append((u, c))

    f.close()
    return Adj, Name, Idx


def print_directed_graph(Adj, Name, Idx):
    for n in Name:
        ie = Idx.get(n)
        print(f"Node {n} has neighbours and weights:")
        for inei in Adj[ie]:
            print(f"Neighbour {Name[inei[0]]} with cost {inei[1]}")

        print()


def plot_directed_graph(Adj, Name, Idx):
    G = nx.DiGraph()

    G.add_nodes_from(Name)

    for n in Name:
        index_v = Idx.get(n)
        for i in range(0, len(Adj[index_v])):
            G.add_edge(n, Name[Adj[index_v][i][0]], weight=Adj[index_v][i][1])

    pos = nx.spring_layout(G, k=0.15, seed=7, iterations=20)
    nx.draw_networkx_nodes(G, pos, node_size=600)
    nx.draw_networkx_edges(G, pos, arrowstyle="-", width=3)
    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.show()


def plot_directed_mst(T, Name, Idx):
    G = nx.DiGraph()

    G.add_nodes_from(Name)

    for i in range(0, len(T)):
        G.add_edge(Name[T[i][1]], Name[T[i][2]], weight=T[i][0])

    pos = nx.spring_layout(G, k=0.15, seed=7, iterations=20)
    nx.draw_networkx_nodes(G, pos, node_size=600)
    nx.draw_networkx_edges(G, pos, arrowstyle="-", width=3)
    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.show()
####


# Disjoint Set Util, not efficient but it gets it done
class disjoint_set:
    def __init__(self):
        self.parent = self


def set_find(s):
    while s.parent != s:
        s = s.parent

    return s


def set_union(a, b):
    while a.parent != a:
        a = a.parent

    while b.parent != b:
        b = b.parent

    a.parent = b
####


def kruskal(Adj, Name, Idx):
    n = len(Name)

    E = []
    for u in range(n):
        for v, c in Adj[u]:
            if u < v:
                # Filters out any duplicate edge, as the undirected graph
                # has the same edge for both vertex index
                E.append((c, u, v))

    # Now E is the collection of all edges
    merge_sort(E, 0, len(E) - 1)

    S = [None]*n
    for u in range(n):
        S[u] = disjoint_set()

    T = [None]*n
    for u in range(n):
        T[u] = []

    for c, u, v in E:
        # edges are already using Idx indexes
        if set_find(S[u]) != set_find(S[v]):
            T[u].append((v, c))
            T[v].append((u, c))

            set_union(S[u], S[v])

    return T


# Merge sorts in place a list of edges by its cost c: (x, y, c)
def merge_sort(E, l, r):
    if l < r:
        m = l + (r - l) // 2

        merge_sort(E, l, m)
        merge_sort(E, m + 1, r)

        merge(E, l, m, r)


def merge(arr, l, m, r):
    l2 = m + 1

    # If the direct merge is already sorted
    if (arr[m][0] <= arr[l2][0]):
        return

    # Two pointers to maintain start
    # of both arrays to merge
    while (l <= m and l2 <= r):

        # If element 1 is in right place
        if (arr[l][0] <= arr[l2][0]):
            l += 1
        else:
            value = arr[l2]
            index = l2

            # Shift all the elements between element 1
            # element 2, right by 1.
            while (index != l):
                arr[index] = arr[index - 1]
                index -= 1

            arr[l] = value

            # Update all the pointers
            l += 1
            m += 1
            l2 += 1


if __name__ == "__main__":
    Adj, Name, Idx = read_undirected_graph_weights(
        "./src/utils/data/undirected_weighted_graph")

    T = kruskal(Adj, Name, Idx)

    print_directed_graph(Adj, Name, Idx)
    plot_directed_graph(T, Name, Idx)
