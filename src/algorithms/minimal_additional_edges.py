# Write an algorithm minimal_additional_edges(G) that takes an
# undirected graph G and returns the minimal number of edges
# that must be added to G to make it connected.

from src.utils.undirected_graph import *
from src.data_structures.queue import Queue


# Complexity O(V + E)
def minimal_additional_edges(Adj, Name, Idx):
    Q = Queue(len(Name))
    V = [False]*len(Name)
    count = 0

    for n in Name:
        ie = Idx.get(n)

        if V[ie] != True:
            Q.enqueue(ie)

            while not Q.is_empty():
                v = Q.dequeue()
                V[v] = True

                for u in Adj[v]:
                    if not V[u]:
                        Q.enqueue(u)

            count += 1

    return count - 1


if __name__ == "__main__":
    Adj, Name, Idx = read_undirected_graph(
        "./src/utils/data/undirected_maximal_connected_subgraph2")
    plot_undirected_graph(Adj, Name, Idx)

    print(minimal_additional_edges(Adj, Name, Idx))
