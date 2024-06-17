# Consider the following algorithm algo_x(A, B) operating on
# two arrays of numbers A and B of equal length:
# Explain what it does
# Analyze complexity
# Write a strictly better algorithm


import numpy as np
import time
import matplotlib.pyplot as plt
from src.algos.quick_sort import quick_sort


# Returns the length of the longest strictly smaller subsequence
# of A found in B
# Complexity: O(n^2) \theta(n*log(n))
def algo_x(A: list[int], B: list[int]):
    x = 0

    for i in range(len(A)):
        k = algo_y(A, B, i)
        if k > x:
            x = k

    return x


def algo_y(A: list[int], B: list[int], i: int):
    k = i
    while k < len(A) and A[k] > B[k]:
        k += 1
    return k - i


# Complexity: O(n)
def better_x(A: list[int], B: list[int]):
    x = 0

    acc = 0
    for i in range(len(A)):
        if B[i] < A[i]:
            acc += 1
        else:
            acc = 0

        if x < acc:
            x = acc

    return x


# Complexity: O(n)
def nlogn(A: list[int]):
    quick_sort(A)


if __name__ == "__main__":
    A = [
        4, 5, 3, 4, 5, 1, 7, 20, 9, 10
    ]
    B = [
        40, 50, 3, 4, 50, 10, 7, 2, 90, 10
    ]

    # 1
    print(algo_x(A, B))
    print(better_x(A, B))

    # 2
    print(algo_x(B, A))
    print(better_x(B, A))

    # Benchmark
    algo_durations = []
    better_durations = []
    nlogn_durations = []

    inputs = []
    for i in range(1, 501):
        inputs.append((np.random.randint(0, i + 1, size=i, dtype=int),
                      np.random.randint(0, i + 1, size=i, dtype=int)))

    i = 0
    for inp in inputs:
        if algo_x(inp[0], inp[1]) != better_x(inp[0], inp[1]):
            print("Error: ", i)
            i += 1

    for inp in inputs:
        tStart = time.perf_counter()
        algo_x(inp[0], inp[1])
        tEnd = time.perf_counter()

        algo_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        better_x(inp[0], inp[1])
        tEnd = time.perf_counter()

        better_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        nlogn(inp[0])
        tEnd = time.perf_counter()

        nlogn_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 500)]

    # Plot array1 and array2
    plt.plot(x, algo_durations, label='algo_x O(n^2)')
    plt.plot(x, better_durations, label='better_x O(n)')
    plt.plot(x, nlogn_durations, label='better_x O(n*log(n))')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'algo_x vs better_x 285')

    plt.legend()
    plt.show()
