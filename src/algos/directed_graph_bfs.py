import networkx as nx
import matplotlib.pyplot as plt

# Breadth First Search, returns an array of least distances of all vertices from a starting index


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


def add_vertex(Adj, Name, Idx, u_name):
    if u_name in Idx:
        u = Idx[u_name]
    else:
        u = len(Adj)
        Adj.append([])
        Name.append(u_name)
        Idx[u_name] = u

    return u


def print_directed_graph(Adj, Name, Idx):
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


def print_directed_graph_distances(Dist, Prev, Name, Idx):
    D = []

    for i in range(len(Dist)):
        D.append((Name[i], Dist[i]))

    for i in range(len(D)):
        for j in range(i + 1, len(D)):
            if D[j - 1][1] >= D[j][1]:
                D[j], D[j-1] = D[j], D[j-1]

    print()
    for i in range(len(D)):
        print(
            f'Node: {D[i][0]} Distance from {D[0][0]}: {
                D[i][1]} Previous node was: {Name[Prev[i]] if Prev[i] else D[0][0]}'
        )
    print()


def bfs_directed_graph(Adj, Name, Idx, startName):
    if startName not in Idx:
        return None

    # Dist is an array of travel distances from the starting node
    Dist = [None]*len(Name)
    Visited = [0]*len(Name)  # 0 not visited, 1 in the queue, 2 visited
    Previous = [None]*len(Name)

    Q = [None]*len(Name)
    head = 0
    tail = 0

    def enqueue(el):
        nonlocal Q
        nonlocal tail
        if is_full():
            return

        Q[tail] = el
        tail = queue_next(tail)

    def dequeue():
        nonlocal Q
        nonlocal head
        if is_empty():
            return

        el = Q[head]
        head = queue_next(head)
        return el

    def is_full():
        nonlocal tail
        nonlocal head
        return head - 1 == tail

    def is_empty():
        nonlocal tail
        nonlocal head
        return head == tail

    def queue_next(idx):
        nonlocal Q
        if idx < len(Q) - 1:
            return idx + 1
        else:
            return 0

    startIdx = Idx.get(startName)
    enqueue(startIdx)
    Visited[startIdx] = 1
    Dist[startIdx] = 0
    while not is_empty():
        iEl = dequeue()
        neighbours = Adj[iEl]

        for n in neighbours:
            if Visited[n] == 0:
                enqueue(n)
                Previous[n] = iEl
                Visited[n] = 1
                Dist[n] = Dist[iEl] + 1

        Visited[iEl] = 2

    return Dist, Previous


if __name__ == "__main__":
    Adj, Name, Idx = read_directed_graph_no_weights(
        "../utils/data/directed_graph_no_weights_no_cycles")

    Dist, Prev = bfs_directed_graph(Adj, Name, Idx, '1')
    print_directed_graph_distances(Dist, Prev, Name, Idx)
    print_directed_graph(Adj, Name, Idx)
