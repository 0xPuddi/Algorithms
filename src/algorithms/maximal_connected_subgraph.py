
# Write an algorithm maximal_connected_subgraph(G) that takes an undirected
# graph G = (V, E) and prints the vertices of a maximal connected subgraph of G.

from src.utils.undirected_graph import read_undirected_graph, plot_undirected_graph


# Space O(n)
def bfs_maximal_connected_subgraph(Adj, Name, Idx):
    n = len(Name)
    V = [False]*n
    Q = [None]*n
    tail = head = 0
    Vertices = []

    def enqueue(el):
        nonlocal Q, tail
        if full():
            return

        Q[tail] = el
        tail = inext(tail)

    def dequeue():
        nonlocal Q, head
        if empty():
            return

        el = Q[head]
        head = inext(head)
        return el

    def empty():
        nonlocal head, tail
        return tail == head

    def full():
        nonlocal head, tail
        return inext(tail) == head

    def inext(i):
        nonlocal Q
        if i == len(Q) - 1:
            return 0
        else:
            return i + 1

    for n in Name:
        ie = Idx.get(n)

        if V[ie] == True:
            continue

        enqueue(ie)
        Vertices_tmp = []

        while not empty():
            ie = dequeue()

            V[ie] = True
            Vertices_tmp.append(ie)

            for u in Adj[ie]:
                if V[u] == False:
                    enqueue(u)

        if len(Vertices_tmp) > len(Vertices):
            Vertices = Vertices_tmp

    return Vertices


# Space O(n)
def bfs_print_maximal_connected_subgraph(Adj, Name, Idx):
    n = len(Name)
    C = [None]*n
    c = None
    max_c = 0
    Q = [None]*n
    tail = head = 0

    def enqueue(el):
        nonlocal Q, tail
        if full():
            return

        Q[tail] = el
        tail = inext(tail)

    def dequeue():
        nonlocal Q, head
        if empty():
            return

        el = Q[head]
        head = inext(head)
        return el

    def empty():
        nonlocal head, tail
        return tail == head

    def full():
        nonlocal head, tail
        return inext(tail) == head

    def inext(i):
        nonlocal Q
        if i == len(Q) - 1:
            return 0
        else:
            return i + 1

    for n in Name:
        ie = Idx.get(n)

        if C[ie] != None:
            continue

        enqueue(ie)
        C[ie] = ie
        count = 0

        while not empty():
            v = dequeue()
            count = count + 1

            for u in Adj[v]:
                if C[u] == None:
                    enqueue(u)
                    C[u] = ie

        if count > max_c:
            max_c = count
            c = ie

    for i in range(len(C)):
        if C[i] == c:
            print(f'{Name[i]} ', end="")

    print()


def dfs_maximal_connected_subgraph(Adj, Name, Idx):
    n = len(Name)
    V = [False]*n
    S = [None]*n
    tos = -1
    Vertices = []

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

    def get():
        nonlocal S, tos
        if empty():
            return

        return S[tos]

    def empty():
        nonlocal tos
        return tos == -1

    def full():
        nonlocal S, tos
        return tos == len(S) - 1

    for n in Name:
        ie = Idx.get(n)

        if V[ie] == True:
            continue

        push(ie)
        Vertices_tmp = []

        while not empty():
            ie = get()

            if V[ie] == True:
                pop()
                continue

            V[ie] = True
            Vertices_tmp.append(ie)

            for u in Adj[ie]:
                push(u)

        if len(Vertices_tmp) > len(Vertices):
            Vertices = Vertices_tmp

    return Vertices


def make_mcs_adj_list(Idxs_mcs, Adj):
    Adj_mcs = []
    for idx in Idxs_mcs:
        while len(Adj_mcs) <= idx:
            Adj_mcs.append([])
        Adj_mcs[idx] = Adj[idx]
    while len(Adj_mcs) < len(Adj):
        Adj_mcs.append([])

    return Adj_mcs


if __name__ == "__main__":
    Adj, Name, Idx = read_undirected_graph(
        "./src/utils/data/undirected_maximal_connected_subgraph")
    plot_undirected_graph(Adj, Name, Idx)

    Idxs_mcs = bfs_maximal_connected_subgraph(Adj, Name, Idx)
    print(Idxs_mcs)
    Adj_mcs = make_mcs_adj_list(Idxs_mcs, Adj)

    plot_undirected_graph(Adj_mcs, Name, Idx, True)

    Adj, Name, Idx = read_undirected_graph(
        "./src/utils/data/undirected_maximal_connected_subgraph2")
    plot_undirected_graph(Adj, Name, Idx)

    Idxs_mcs = bfs_maximal_connected_subgraph(Adj, Name, Idx)
    print(Idxs_mcs)
    Adj_mcs = make_mcs_adj_list(Idxs_mcs, Adj)

    plot_undirected_graph(Adj_mcs, Name, Idx, True)

    Idxs_mcs = dfs_maximal_connected_subgraph(Adj, Name, Idx)
    print(Idxs_mcs)
    Adj_mcs = make_mcs_adj_list(Idxs_mcs, Adj)

    plot_undirected_graph(Adj_mcs, Name, Idx, True)

    bfs_print_maximal_connected_subgraph(Adj, Name, Idx)
