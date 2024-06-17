# A social network N is defined by a set of users U and by a
# constant-time function F(u1, u2) that tells whether users
# u1 and u2 are “friends”. We say that a social network can be
# covered by a social circle of diameter D ≥ 1 when, for all
# pairs of users a and b, either F(a, b) or there is a chain
# u1, u2, . . . , uk of k < D other users such that F(a, u1),
# F(u1, u2), . . . , F(uk, b). Given a social network N = (U, F)
# and a number d, consider the problem of determining whether
# the social network can be covered by a social circle of diameter d.
# Write a solution algorithm
# Write a resolution algorithm


from src.utils.undirected_graph import read_undirected_graph, plot_undirected_graph
from src.data_structures.queue import Queue
import math


# If P is True checks if there are any path that is greater than d
# If P is False checks if there are any path that is greater than d
def social_circle_diameter_solution(Adj: list[list[int]], Name: list[str], Idx: dict, diameter: int, P: bool) -> bool:
    return P == social_circle_diameter_resolution(Adj, Name, Idx, diameter)


def social_circle_diameter_resolution(Adj: list[list[int]], Name: list[str], Idx: dict, diameter: int) -> bool:
    Q = Queue(len(Name))
    sp = 0

    for n in Name:
        D = [None]*len(Name)
        ie = Idx.get(n)
        D[ie] = 0
        Q.enqueue(ie)

        while not Q.is_empty():
            v = Q.dequeue()

            for u in Adj[v]:
                if D[u] == None:
                    D[u] = D[v] + 1
                    Q.enqueue(u)

        for d in D:
            if d > sp:
                sp = d

    return sp - 1 <= diameter


if __name__ == "__main__":
    Adj, Name, Idx = read_undirected_graph(
        "src/utils/data/undirected_diameter_connected_graph")
    plot_undirected_graph(Adj, Name, Idx)

    d = 2  # False
    print(social_circle_diameter_resolution(Adj, Name, Idx, d))
    print(social_circle_diameter_solution(Adj, Name, Idx, d, True))

    d = 3  # True
    print(social_circle_diameter_resolution(Adj, Name, Idx, d))
    print(social_circle_diameter_solution(Adj, Name, Idx, d, True))

    Adj, Name, Idx = read_undirected_graph(
        "src/utils/data/undirected_diameter_connected_graph2")
    plot_undirected_graph(Adj, Name, Idx)

    d = 2  # True
    print(social_circle_diameter_resolution(Adj, Name, Idx, d))
    print(social_circle_diameter_solution(Adj, Name, Idx, d, True))

    d = 1  # False
    print(social_circle_diameter_resolution(Adj, Name, Idx, d))
    print(social_circle_diameter_solution(Adj, Name, Idx, d, True))
