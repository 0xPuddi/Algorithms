# The following algorithm takes an array A of numbers:
# Explain what it does
# Analyze complexity
# Write a strictly better algorithm


import numpy as np
import time
import matplotlib.pyplot as plt
from src.algos.quick_sort import quick_sort
from random import shuffle


# Finds and returns the most often occuring elements. From smaller
# to greater
# Complexity: O(n^2)
def algo_x(A: list[int]):
    if len(A) == 1:
        return A

    B = [None] * len(A)
    l = 0
    m = 0

    for i in range(len(A)):
        k = 0

        for j in range(i + 1, len(A)):
            if A[i] == A[j]:
                k += 1

        if m < k:
            l = 0
            m = k
            B[l] = A[i]
        elif m == k:
            l = l + 1

            if l == len(B):
                B.append(A[i])
            else:
                B[l] = A[i]

    L = []
    if l == len(B):
        L = B[1:l]
    else:
        L = B[:l+1]

    if L[0] == None:
        L = L[:1]

    L.sort()
    return L


# Complexity: O(n*log(n))
def better_x(A: list[int]):
    if len(A) == 1:
        return A

    quick_sort(A)

    L = []
    often = 0
    acc = 0
    for i in range(len(A) - 1):
        if A[i] == A[i+1]:
            if acc == 0:
                acc += 2
            else:
                acc += 1

            if acc == often:
                L.append(A[i])

            if acc > often:
                often = acc
                L = []
                L.append(A[i])
        elif A[i] != A[i+1]:
            acc = 0

    return L if len(L) != 0 else [None]


if __name__ == "__main__":
    A = [
        1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 5, 5
    ]

    # 2 3 5
    print(algo_x(A))
    print(better_x(A))

    # Benchmark
    algo_durations = []
    better_durations = []

    inputs = []
    for i in range(1, 501):
        inputs.append(np.random.randint(0, i + 1, size=i, dtype=int))

    i = 0
    for inp in inputs:
        if algo_x(inp) != better_x(inp):
            print("Error: ", i)
            i += 1

    for inp in inputs:
        tStart = time.perf_counter()
        algo_x(inp)
        tEnd = time.perf_counter()

        algo_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        better_x(inp)
        tEnd = time.perf_counter()

        better_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 500)]  # Range from 0 to 300 inclusive

    # Plot array1 and array2
    plt.plot(x, algo_durations, label='algo_x O(n^2)')
    plt.plot(x, better_durations, label='better_x O(n*log(n))')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'algo_x vs better_x 281')

    plt.legend()
    plt.show()
