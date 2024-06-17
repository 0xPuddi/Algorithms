# Make graphing util

import networkx as nx
import matplotlib.pyplot as plt


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


def read_undirected_graph(filename):
    f = open(filename)
    Name = []
    Idx = {}
    Adj = []

    for l in f:
        u_name, v_name = l.strip().split()
        u = add_vertex(Adj, Name, Idx, u_name)
        v = add_vertex(Adj, Name, Idx, v_name)

        Adj[u].append(v)
        Adj[v].append(u)

    f.close()
    return Adj, Name, Idx


def add_vertex(Adj, Name, Idx, u_name):
    if u_name in Idx:
        u = Idx[u_name]
    else:
        u = len(Adj)
        Adj.append([])
        Name.append(u_name)
        Idx[u_name] = u

    return u


def print_directed_graph_weights(Adj, Name, Idx):
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
                f"Neighbour node {Name[inei[0]]}, index {inei[0]}"
            )

        print()


def plot_directed_graph_weight(Adj, Name, Idx):
    G = nx.DiGraph()

    G.add_nodes_from(Name)

    for n in Name:
        index_v = Idx.get(n)
        for i in range(0, len(Adj[index_v])):
            G.add_edge(n, Name[Adj[index_v][i][0]], weight=Adj[index_v][i][1])

    pos = nx.spring_layout(G, k=0.15, seed=7, iterations=20)
    nx.draw_networkx_nodes(G, pos, node_size=600)
    nx.draw_networkx_edges(G, pos, arrowstyle="->", width=3)
    nx.draw_networkx_labels(G, pos, font_size=15, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.show()


def plot_undirected_graph_weight(Adj, Name, Idx):
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


def plot_undirected_graph(Adj, Name, Idx, hide_alone_vertex=False):
    G = nx.DiGraph()

    edges = []
    nodes = []
    for n in Name:
        if n not in Idx:
            continue

        index_v = Idx.get(n)

        if hide_alone_vertex:
            if len(Adj[index_v]) != 0:
                nodes.append(n)
        else:
            nodes.append(n)

        for i in range(0, len(Adj[index_v])):
            edges.append((n, Name[Adj[index_v][i]]))

    G.add_edges_from(edges)
    G.add_nodes_from(nodes)

    nx.draw(G, with_labels=True,
            pos=nx.spring_layout(G, k=0.15, iterations=20), arrows=False, node_size=1000)
    plt.show()
