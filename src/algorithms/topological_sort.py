

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


def read_directed_graph_no_weights(filename):
    f = open(filename)
    Name = []
    Idx = {}
    Adj = []

    for l in f:
        u_name, v_name = l.strip().split()
        u = add_vertex(Adj, Name, Idx, u_name)
        v = add_vertex(Adj, Name, Idx, v_name)

        Adj[u].append(v)

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
                f"Neighbour node {Name[inei]}, index {inei}"
            )

        print()


def plot_directed_graph(Adj, Name, Idx):
    G = nx.DiGraph()

    G.add_nodes_from(Name)

    edges = []
    for n in Name:
        index_v = Idx.get(n)
        for i in range(0, len(Adj[index_v])):
            edges.append((n, Name[Adj[index_v][i]]))

    G.add_edges_from(edges)

    nx.draw(G, with_labels=True,
            pos=nx.spring_layout(G, k=0.15, iterations=20), node_size=1000)
    plt.show()


def TO_to_names(TO, Name):
    print()
    print()
    print("Printing a TO")
    print()

    for i, t in enumerate(TO):
        if i == len(TO) - 1:
            print(f"{Name[t]}", end="")
            break

        print(f"{Name[t]} -> ", end="")
    print()

####


def topological_sort_recursive(Adj, Name, Idx):
    n = len(Name)

    TO = [None]*n       # Topolodical Ordered array
    to = len(TO) - 1
    V = [0]*n           # Visited Nodes by Idx

    def add_to(ie):
        nonlocal TO, to

        TO[to] = ie
        to = to - 1

    def recurse(ie):
        nonlocal V

        V[ie] = 1

        for nei in Adj[ie]:
            if V[nei] == 0:
                recurse(nei)

        V[ie] = 2
        add_to(ie)

    for n in Name:
        ie = Idx.get(n)

        if V[ie] != 0:
            continue

        recurse(ie)

    return TO


def topological_sort_iterative(Adj, Name, Idx):
    n = len(Name)

    TO = [None]*n       # Topolodical Ordered array
    to = len(TO) - 1
    V = [0]*n           # Visited Nodes by Idx
    S = [None]*n
    tos = -1

    def add_to(ie):
        nonlocal TO, to

        TO[to] = ie
        to = to - 1

    # Stack
    def get():
        nonlocal S, tos
        if empty():
            return

        return S[tos]

    def push(el):
        nonlocal S, tos
        if full():
            return

        tos += 1
        S[tos] = el

    def pop():
        nonlocal S, tos

        if empty():
            return

        el = S[tos]
        tos -= 1
        return el

    def empty():
        nonlocal tos
        return tos == -1

    def full():
        nonlocal S, tos
        return tos == len(S) - 1
    ####

    for n in Name:
        ie = Idx.get(n)

        if V[ie] != 0:
            continue

        push(ie)
        while not empty():
            ie = get()

            if V[ie] == 0:
                V[ie] = 1

                for u in Adj[ie]:
                    if V[u] == 0:
                        push(u)
            elif V[ie] == 1:
                V[ie] = 2
                add_to(ie)
            elif V[ie] == 2:
                pop()

    return TO


if __name__ == "__main__":
    Adj, Name, Idx = read_directed_graph_no_weights(
        "./src/utils/data/dag_no_weights")
    print_directed_graph(Adj, Name, Idx)
    plot_directed_graph(Adj, Name, Idx)

    TO_to_names(topological_sort_recursive(Adj, Name, Idx), Name)
    TO_to_names(topological_sort_iterative(Adj, Name, Idx), Name)

    Adj, Name, Idx = read_directed_graph_no_weights(
        "./src/utils/data/dag_no_weights2")
    print_directed_graph(Adj, Name, Idx)
    plot_directed_graph(Adj, Name, Idx)

    TO_to_names(topological_sort_recursive(Adj, Name, Idx), Name)
    TO_to_names(topological_sort_iterative(Adj, Name, Idx), Name)
