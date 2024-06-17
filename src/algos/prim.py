

# Find a minimum spanning tree of a weighted undirected graph, using prim's algorithm
# Prim's algorithm


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


# Priority Queue
# Val is made out of (previous_edge, edge, cost): we use cost has priority value
def min_enqueue(Q, edge):
    i = len(Q)
    Q.append(edge)

    while i > 0:
        i = parent(i)
        min_heapify_down(Q, i)

        # Nothing changes after heapifying down
        if Q[i] != edge:
            return


def min_dequeue(Q):
    # We extraxt most priority element
    m = Q[0]

    # We bring last leaf as root and delete it
    Q[0] = Q[-1]
    Q.pop()

    # We min-heapify down new root
    min_heapify_down(Q, 0)

    # We return element
    return m


def min_update_key(Q, edge):
    # Look for the key
    i = min_find_vertices(Q, edge)

    # Key does not exist, we enqueue it
    if i == None:
        min_enqueue(Q, edge)
        return

    # Key exists and does not have less priority: we exit
    if Q[i][2] < edge[2]:
        return

    # Key exists and has less priority: we update it
    Q[i] = edge

    # Three cases:
    # 1. It is smaller than the parent: We heapify up
    # 2. It is greater than children: We heapify down
    # 3. None of the above: we exit

    # Case 1
    p = parent(i)
    if p >= 0 and Q[p][2] > Q[i][2]:
        while i > 0:
            i = parent(i)
            min_heapify_down(Q, i)
        return

    # Case 2
    lc = left_child(i)
    rc = left_child(i)
    if (lc < len(Q) or rc < len(Q)) and (Q[lc][2] < Q[i][2] or Q[rc][2] < Q[i][2]):
        min_heapify_down(Q, i)

    # Case 3


def min_find_vertices(Q, edge):
    ie = None
    ue, ve, ce = edge

    for i in range(len(Q)):
        u, v, c = Q[i]
        if v == ve:
            ie = i
            break

    return ie


def min_heapify_down(Q, root):
    while left_child(root) < len(Q):
        m = root
        lc = left_child(root)
        rc = right_child(root)

        # left child higher priority
        if Q[lc][2] < Q[m][2]:
            m = lc

        # right child higher priority
        if rc < len(Q) and Q[rc][2] < Q[m][2]:
            m = rc

        # No children with higher priority
        if m == root:
            return

        # Swap
        Q[root], Q[m] = Q[m], Q[root]

        # Traverse to new position in the queue of m
        root = m


def parent(i):
    return (i - 1) // 2


def left_child(i):
    return 2*i + 1


def right_child(i):
    return 2*i + 2
####


def prim(Adj, Name, Idx):
    n = len(Name)

    T = [None]*n  # MST edges by Idx
    for v in range(n):
        T[v] = []

    Q = []  # Priority Queue

    # Proceed BFS, we warm the queue by enqueueing
    # vertex at index 0, from None vertex at a 0.0 cost
    min_enqueue(Q, (None, 0, 0.0))

    V = [False]*n  # Visited list

    while len(Q) != 0:
        p, v, c = min_dequeue(Q)

        # When an edge v that has been already added to the tree
        if V[v]:
            continue

        V[v] = True

        if p != None:
            T[p].append((v, c))
            T[v].append((p, c))
            V[p] = True

        for v2, c2 in Adj[v]:
            # If you find already the edge, update it if it
            # has a better cost, otherwise add it to the queue
            if not V[v2]:
                min_update_key(Q, (v, v2, c2))

    return T


if __name__ == "__main__":
    Adj, Name, Idx = read_undirected_graph_weights(
        "./src/utils/data/undirected_weighted_graph")
    print_directed_graph(Adj, Name, Idx)
    plot_directed_graph(Adj, Name, Idx)

    T = prim(Adj, Name, Idx)
    plot_directed_graph(T, Name, Idx)

    Adj, Name, Idx = read_undirected_graph_weights(
        "./src/utils/data/undirected_weighted_graph2")
    print_directed_graph(Adj, Name, Idx)
    plot_directed_graph(Adj, Name, Idx)

    T = prim(Adj, Name, Idx)
    plot_directed_graph(T, Name, Idx)
