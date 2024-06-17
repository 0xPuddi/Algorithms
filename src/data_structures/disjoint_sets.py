

import networkx as nx
import matplotlib.pyplot as plt


# Disjoint sets data structure, constructor is O(n), while everythins is ammortized \alpha(n) if you use compressed path methods, otherwise O(n)

def construct(objects):
    A = []
    S = []
    M = {}
    Name = []

    for o in objects:
        M[o] = len(A)
        A.append(len(A))
        Name.append(o)
        S.append(1)

    return A, M, S, Name


def union(x, y, A, M, S):
    x = M.get(x)
    while x != A[x]:
        x = A[x]

    y = M.get(y)
    while y != A[y]:
        y = A[y]

    A[y] = x
    S[x] += S[y]


def union_compress(x, y, A, M, S):
    root_x = find_compress(x, A, M)
    root_y = find_compress(y, A, M)

    if root_x == root_y:
        return

    # Merge smaller to bigger
    if S[root_x] <= S[root_y]:
        S[root_y] += S[root_x]
        A[root_x] = root_y
    else:
        S[root_x] += S[root_y]
        A[root_y] = root_x


def find_compress(x, A, M):
    x = M.get(x)
    root = x
    while root != A[root]:
        root = A[root]

    while x != root:
        nxt = A[x]
        A[x] = root
        x = nxt

    return x


def find(x, A, M):
    x = M.get(x)
    while x != A[x]:
        x = A[x]

    return x


def get_component_size(x, A, M, S):
    return S[find(x, A, M)]


def get_component_size_compress(x, A, M, S):
    return S[find_compress(x, A, M)]


def get_component_number(A):
    acc = 0

    for i in A:
        if i == A[i]:
            acc = acc + 1

    return acc


def get_elements_number(A):
    return len(A)


def check_same_component(x, y, A, M):
    x = M.get(x)
    while x != A[x]:
        x = A[x]

    y = M.get(y)
    while y != A[y]:
        y = A[y]

    return x == y


def check_same_component_compress(x, y, A, M):
    return find_compress(x, A, M) == find_compress(y, A, M)


def plot_disjoint_set(A, M, Name):
    G = nx.DiGraph()

    edges = []
    for m in M:
        G.add_nodes_from(m)

        parent = A[M.get(m)]
        edges.append((m, Name[A[M.get(m)]]))

    G.add_edges_from(edges)

    nx.draw(G, with_labels=True,
            pos=nx.spring_layout(G, k=0.15, iterations=20), node_size=1000)
    plt.show()
    return


if __name__ == "__main__":
    A, M, S, Name = construct((
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
    ))

    print(get_component_number(A))
    print(find('C', A, M))
    union_compress('C', 'B', A, M, S)
    union_compress('D', 'B', A, M, S)
    union_compress('D', 'A', A, M, S)
    print(get_component_size('A', A, M, S))
    print(check_same_component('A', 'C', A, M))

    plot_disjoint_set(A, M, Name)
