import networkx as nx
import matplotlib.pyplot as plt

# Find loops with Depth First Search, returns


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


def directed_graph_iterative_shortest_path(Adj, Name, Idx, startName, endName):
    v = len(Name)
    # Index based, if the node has not been visited (0), it has been visited (1), it is done (2)
    V = [0]*v
    P = [None]*v

    # QUEUE
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
    ###

    startIdx = Idx.get(startName)
    endIdx = Idx.get(endName)
    enqueue(startIdx)
    V[startIdx] = 1

    while not is_empty():
        u = dequeue()

        for nei in Adj[u]:
            if V[nei] == 0:
                V[nei] = 1
                P[nei] = u
                enqueue(nei)

        V[u] = 2

    # add path from end
    sp = []
    sp.append(endIdx)
    prev = P[endIdx]
    while prev != None:
        sp.append(prev)
        prev = P[prev]

    sp.reverse()

    if sp[0] == startIdx:
        return sp

    return []


if __name__ == "__main__":
    Adj, Name, Idx = read_directed_graph_no_weights(
        "./src/utils/data/directed_graph_no_weights_no_cycles")

    sp = directed_graph_iterative_shortest_path(Adj, Name, Idx, '1', '8')
    print(Idx)
    print(sp)
    print_directed_graph(Adj, Name, Idx)
