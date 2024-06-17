

# Find a minimum spanning tree of a weighted undirected graph, using prim's algorithm
# Prim's algorithm


import networkx as nx
import matplotlib.pyplot as plt
import math


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


def read_directed_graph_weights(filename):
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

    f.close()
    return Adj, Name, Idx


def print_directed_graph(Adj, Name, Idx):
    print()
    print()
    print("Printing a graph")
    print()

    for n in Name:
        ie = Idx.get(n)
        print(f"Node {n}, index {ie} has neighbours and weights:")
        for inei in Adj[ie]:
            print(
                f"Neighbour node {Name[inei[0]]}, index {
                    inei[0]} with cost {inei[1]}"
            )

        print()


def plot_directed_graph(Adj, Name, Idx):
    G = nx.DiGraph()

    G.add_nodes_from(Name)

    for n in Name:
        index_v = Idx.get(n)
        for i in range(0, len(Adj[index_v])):
            G.add_edge(n, Name[Adj[index_v][i][0]], weight=Adj[index_v][i][1])

    pos = nx.spring_layout(G, k=0.15, seed=7, iterations=20)
    nx.draw_networkx_nodes(G, pos, node_size=400)
    nx.draw_networkx_edges(G, pos, arrowstyle="->", width=1)
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
    nx.draw_networkx_nodes(G, pos, node_size=400)
    nx.draw_networkx_edges(G, pos, arrowstyle="->", width=1)
    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.show()
####


def topological_sort(Adj, Name, Idx):
    n = len(Name)
    V = [0]*n

    TO = [None]*n
    to = len(TO) - 1

    def add_TO(i):
        nonlocal TO, to

        TO[to] = i
        to = to - 1

    def recurse(i):
        nonlocal V
        V[i] = 1

        for u, c in Adj[i]:
            if V[u] == 0:
                recurse(u)

        V[i] = 2
        add_TO(i)

    for n in Name:
        ie = Idx.get(n)

        if V[ie] == 0:
            recurse(ie)

    return TO


def longest_path_dag(Adj, Name, Idx):
    n = len(Name)
    D = [math.inf]*n
    TO = topological_sort(Adj, Name, Idx)

    D[TO[0]] = 0
    for t in TO:
        for u, c in Adj[t]:
            if D[u] > D[t] + -1 * c:
                D[u] = D[t] + -1 * c

    for i in range(len(D)):
        D[i] = D[i] * -1

    return D


if __name__ == "__main__":
    Adj, Name, Idx = read_directed_graph_weights(
        "./src/utils/data/dag_weights_negative")
    print_directed_graph(Adj, Name, Idx)
    plot_directed_graph(Adj, Name, Idx)

    D = longest_path_dag(Adj, Name, Idx)
    for i, c in enumerate(D):
        print(f"Name {Name[i]}, Cost {c}")
