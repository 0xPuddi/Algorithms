

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


def bellman_ford(Adj, Name, Idx, startName):
    n = len(Name)

    T = [None]*n  # MST edges by Idx
    for v in range(n):
        T[v] = []

    D = [math.inf]*n    # Distance cost based on Idx vertex
    P = [None]*n        # Previous vertex based on Idx

    startIdx = Idx.get(startName)

    # Iterate over each possible |V| - 1 edges path
    D[startIdx] = 0
    for _ in range(n - 1):
        for idx, edges in enumerate(Adj):
            for e in edges:
                if D[idx] != math.inf and D[e[0]] > D[idx] + e[1]:
                    D[e[0]] = D[idx] + e[1]
                    P[e[0]] = idx

    # Recunstruct edges and their cost
    for i in range(n):
        p = P[i]
        if p == None:
            continue

        T[p].append((i, D[i]))

    return T


if __name__ == "__main__":
    Adj, Name, Idx = read_directed_graph_weights(
        "./src/utils/data/directed_weighted_negatives_cycle_graph")
    print_directed_graph(Adj, Name, Idx)
    plot_directed_graph(Adj, Name, Idx)

    T = bellman_ford(Adj, Name, Idx, 's')
    plot_directed_graph(T, Name, Idx)
