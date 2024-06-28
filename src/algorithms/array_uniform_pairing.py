# Given an array A of 2n numbers, a pairing over A is a set of n pairs formed
# from the elements of A, such that each element A[i] appears in exactly one pair. For example,
# given the array A = [1, 0, 3, 7, 3, 2], a valid pairing could be (1, 3), (3, 7), (2, 0).
# Consider the following decision problem. Given an array A of 2n numbers, output “yes” if there
# exists a uniform pairing over A, meaning a pairing in which all the pairs have the same total value.
# The total value of a pair is simply the sum of its two elements. For example, the pairing given
# above is not uniform, since the total values of its three pairs are 4, 10, and 2, respectively.
# Is the problem in NP? Write an algorithm that proves it, or argue the opposite.
# Is the problem in P? Write an algorithm that proves it, or argue the opposite.


import numpy as np
import time
import matplotlib.pyplot as plt
from src.algos.quick_sort import quick_sort


# Checks whether pairs are uniform
# Time Complexity: O(3n) = O(n)
# Space Complexity: O(n)
def pairing_solution(A: list[int], P: list[(int, int)]):
    if len(P) == 0:
        return False

    S = {}
    for i in range(len(A)):
        if A[i] not in S:
            S[A[i]] = 1
        else:
            S[A[i]] += 1

    for i in range(len(P)):
        if P[i][0] in S:
            S[P[i][0]] -= 1

        if P[i][1] in S:
            S[P[i][1]] -= 1

    for s in S:
        if S[s] != 0:
            return False

    uniform_sum = P[0][0] + P[0][1]
    for i in range(len(P)):
        if uniform_sum != (P[i][0] + P[i][1]):
            return False

    return True


# Time Complexity: O(n*log(N))
def pairing_resolution(A: list[int]):
    quick_sort(A)

    unform_sum = A[0] + A[-1]
    for i in range(1, len(A) // 2):
        if (A[i] + A[len(A) - 1 - i]) != unform_sum:
            return False

    return True


if __name__ == "__main__":
    A = [
        1, 0, 3, 7, 3, 2
    ]
    PA = [
        (1, 3),
        (3, 7),
        (2, 0)
    ]

    B = [
        2, 2, 2, 2, 2, 2
    ]
    PB = [
        (2, 2),
        (2, 2),
        (2, 2)
    ]

    C = [
        2, 3, 5, 0, 4, 1
    ]
    PC = [
        (2, 3),
        (5, 0),
        (4, 1)
    ]

    print(pairing_solution(A, PA))
    print(pairing_solution(B, PB))
    print(pairing_solution(C, PC))

    print(pairing_resolution(A))
    print(pairing_resolution(B))
    print(pairing_resolution(C))

    # Benchmark
    durations = []

    inputs = []
    for i in range(1, 501):
        inputs.append(np.random.randint(0, i + 1, size=i, dtype=int))

    for inp in inputs:
        tStart = time.perf_counter()
        pairing_resolution(inp)
        tEnd = time.perf_counter()

        durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 500)]

    # Plot array1 and array2
    plt.plot(x, durations, label='pairing_resolution O(n*log(n))')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'pairing_resolution')

    plt.legend()
    plt.show()
