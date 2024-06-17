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


def dfs_directed_graph_recursive(Adj, Name, Idx):
    # Broken

    v = len(Name)
    D = [None]*v  # Index based, at which time it is discovered
    P = [None]*v  # Index based, from which vertex we come
    F = [None]*v  # Index based, at which time it is completed
    # Index based, if the node has not been visited (0), it has been visited (1), it is done (2)
    V = [0]*v

    time = 0  # Global time variable

    def recurse(ie):
        nonlocal D, P, F, V, time, Adj

        V[ie] = 1
        time = time + 1
        D[ie] = time

        for i in Adj[ie]:
            if V[i] == 1:
                return True

            if V[i] == 0:
                P[i] = ie
                recurse(i)

        V[ie] = 2
        time = time + 1
        F[ie] = time

    for n in Name:
        if n in Idx:
            is_loop = False

            if V[Idx.get(n)] == 0:
                is_loop = recurse(Idx.get(n))

            if is_loop == True:
                return is_loop

    return False


def dfs_directed_graph_iterative(Adj, Name, Idx):
    v = len(Name)
    D = [None]*v  # Index based, at which time it is discovered
    P = [None]*v  # Index based, from which vertex we come
    F = [None]*v  # Index based, at which time it is completed
    # Index based, if the node has not been visited (0), it has been visited (1), it is done (2)
    V = [0]*v

    time = 0  # Global time variable

    S = [None]*v  # Stack
    top = -1  # Top of Stack

    # Pushes element on top of stack
    def push(el):
        nonlocal S
        nonlocal top

        if top == len(S) - 1:
            return

        top = top + 1
        S[top] = el

    # Pops element on top of stack and returns it
    def pop():
        nonlocal S
        nonlocal top

        if is_empty():
            return

        el = S[top]
        top = top - 1

        return el

    def get():
        nonlocal S, top
        return S[top]

    def is_empty():
        nonlocal S
        return top == -1

    for n in Name:
        if n not in Idx:
            return False

        if D[Idx.get(n)] != None:
            continue

        ie = Idx.get(n)
        push(ie)

        while not is_empty():
            u = get()

            if D[u] == None:
                V[u] = 1
                D[u] = time
                time = time + 1

                for nei in Adj[u]:
                    if D[nei] == None:
                        push(nei)
                        P[nei] = u

                    # We see a node that has been seen but\
                    # not yet completed: There is a loop
                    if V[nei] == 1:
                        return True

            elif F[u] == None:
                F[u] = time
                time = time + 1
                V[u] = 2
            else:
                pop()

    return False


def dfs_directed_graph_iterative_visited(Adj, Name, Idx):
    v = len(Name)
    # Index based, if the node has not been visited (0), it has been visited (1), it is done (2)
    V = [0]*v

    S = [None]*v  # Stack
    top = -1  # Top of Stack

    # Pushes element on top of stack
    def push(el):
        nonlocal S
        nonlocal top

        if top == len(S) - 1:
            return

        top = top + 1
        S[top] = el

    # Pops element on top of stack and returns it
    def pop():
        nonlocal S
        nonlocal top

        if is_empty():
            return

        el = S[top]
        top = top - 1

        return el

    def get():
        nonlocal S, top
        return S[top]

    def is_empty():
        nonlocal S
        return top == -1

    for n in Name:
        if n not in Idx:
            return False

        if V[Idx.get(n)] != 0:
            continue

        ie = Idx.get(n)
        push(ie)

        while not is_empty():
            u = get()

            if V[u] == 0:
                V[u] = 1

                for nei in Adj[u]:
                    if V[nei] == 0:
                        push(nei)

                    # We see a node that has been seen but\
                    # not yet completed: There is a loop
                    if V[nei] == 1:
                        return True

            elif V[u] == 1:
                V[u] = 2
            else:
                pop()

    return False


if __name__ == "__main__":
    Adj, Name, Idx = read_directed_graph_no_weights(
        "./src/utils/data/directed_graph_no_weights_cycle")

    print(dfs_directed_graph_iterative(Adj, Name, Idx))
    print(dfs_directed_graph_iterative_visited(Adj, Name, Idx))
    print(Idx)
    # print(dfs_directed_graph_recursive(Adj, Name, Idx))
    print_directed_graph(Adj, Name, Idx)
