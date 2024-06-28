# Consider the following algorithm Algo-X(A, B) operating on two
# arrays of numbers A and B of total length A.length + B.length = n:
# Explain what it does
# Analyze complexity
# Write a strictly better algorithm


import numpy as np
import time
import matplotlib.pyplot as plt
from src.algos.quick_sort import quick_sort
from random import shuffle


# Returns the maximal length of any contiguous subsequence of A whose
# total value is equal to an element of B. If no such sequence exists,
# the result is 0.
# Complexity: O(n^4)
def algo_x(A: list[int], B: list[int]):
    for l in range(len(A) - 1, -1, -1):
        for j in range(len(B)):
            for i in range(0, len(A) - l + 1):
                s = 0
                for k in range(i, i + l - 1):
                    s = s + A[k]

                if s == B[j]:
                    return l
    return 0


# Complexity: O(n^2)
def better_x(A: list[int], B: list[int]):
    max_l = 0
    for i in range(len(B)):
        s = 0
        for j in range(len(A)):
            s = s + A[j]

            if s == B[i] and j > max_l:
                print("For: ", B[i])
                max_l = j

    return max_l


if __name__ == "__main__":
    A = [
        1, 1, 1, 1, 1, 1, 1, 1, 1
    ]
    B = [
        10, 4, 5, 6, 7
    ]

    C = [
        9, 1, 2, 3, 4, 5
    ]
    D = [
        10, 4, 5, 6, 24
    ]

    print(algo_x(A, B))
    print(algo_x(C, D))
    print(better_x(A, B))
    print(better_x(C, D))
