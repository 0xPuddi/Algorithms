# The following algorithm takes an array A of n numbers:
# Explain what it does
# Analyze complexity
# Write a strictly better algorithm


import numpy as np
import time
import matplotlib.pyplot as plt
from src.algos.quick_sort import quick_sort
from random import shuffle


# Counts how many unique elements there are in the array
# Complexity: O(n^2)
def algo_x(A: list[int]):
    n = len(A)
    x = 0

    for i in range(n):
        j = 0
        while j < n and (i == j or A[i] != A[j]):
            j += 1

        if j >= n:
            x += 1

    return x


# Complexity: O(n*log(n))
def better_x(A: list[int]):
    if len(A) == 1:
        return 1

    A.sort()

    x = 0

    if A[0] != A[1]:
        x += 1

    for i in range(1, len(A)):
        if i == len(A) - 1 and A[i - 1] != A[i]:
            x += 1
        elif A[i - 1] != A[i] and A[i] != A[i + 1]:
            x += 1

    return x


if __name__ == "__main__":
    A = [
        4, 5, 3, 4, 5, 1, 7, 2, 9, 10
    ]

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
        'algo_x vs better_x 287')

    plt.legend()
    plt.show()
