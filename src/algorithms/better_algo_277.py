# Consider the following algorithm that takes an array A of numbers:
# Explain what it does
# Analyze complexity
# Write a strictly better algorithm


import numpy as np
import time
import matplotlib.pyplot as plt
from src.algos.quick_sort import quick_sort


# Returns the ordered sequences of the most recurring elements
# Complexity: O(n^2)
def algo_x(A: list[int]):
    B = [None] * len(A)
    l = 0

    for i in range(len(A)):
        k = 1

        for j in range(i + 1, len(A)):
            if A[i] == A[j]:
                k += 1

        if l == 0 or B[l] == None or B[l] < k:
            l = 1
            if len(B) - 1 < l:
                B.append(A[i])
            else:
                B[l] = A[i]
        elif B[l] == k:
            l += 1
            if len(B) - 1 < l:
                B.append(A[i])
            else:
                B[l] = A[i]

    L = B[:l+1]
    if L[0] == None:
        L = L[1:]

    L.sort()
    return L


# Complexity: O(n*log(n))
def better_x(A: list[int]):
    if len(A) == 1:
        return A

    quick_sort(A)

    M = []
    max_recurrence = 0
    recurrence = 0
    last_v = A[0]
    for i in range(len(A)):
        if A[i] == last_v:
            recurrence += 1
        elif A[i] != last_v:
            last_v = A[i]
            recurrence = 1

        if recurrence > max_recurrence:
            M = []
            M.append(A[i])
            max_recurrence = recurrence
        elif recurrence == max_recurrence:
            M.append(A[i])

    return M


if __name__ == "__main__":
    A = [
        4, 5, 3, 4, 5, 1, 7, 20, 9, 10
    ]
    B = [
        2, 50, 50, 2, 40, 50, 3, 4, 2, 50, 10, 7, 7, 2, 90, 10, 10
    ]

    # A
    print(algo_x(A))
    print(better_x(A))

    # B
    print(algo_x(B))
    print(better_x(B))

    # Benchmark
    algo_durations = []
    better_durations = []

    inputs = []
    for i in range(1, 501):
        inputs.append(np.random.randint(0, i + 1, size=i, dtype=int))

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

    x = [i for i in range(0, 500)]

    # Plot array1 and array2
    plt.plot(x, algo_durations, label='algo_x O(n^2)')
    plt.plot(x, better_durations, label='better_x O(n*log(n))')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'algo_x vs better_x 277')

    plt.legend()
    plt.show()
