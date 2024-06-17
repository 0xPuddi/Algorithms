
import numpy as np
import matplotlib.pyplot as plt
import time


# Complexity O(n^2)
def algo_x(A, k):
    n = len(A)
    for i in range(n):
        x = 0
        y = 0
        r = 0
        for j in range(n):
            if A[j] < A[i]:
                x = x + 1
                r = r + A[j]
            elif A[j] == A[i]:
                y = y + 1

        if x <= k and x + y >= k:
            return r + A[i]*(k - x)
    return None


# Complexity O(log(n))
def better_x_partition(A, k):
    if k > len(A) or k == 0:
        return None

    iel = partition(A, 0, len(A) - 1)
    lb = 0
    hb = len(A) - 1
    while iel != k - 1:
        if iel < k - 1:
            lb = iel + 1
        elif iel > k - 1:
            hb = iel - 1

        iel = partition(A, lb, hb)

    s = 0
    for i in range(k):
        s = s + A[i]

    return s


# Complexity O(n*log(n))
def better_x(A, k):
    if k > len(A):
        return None

    quick_sort(A)

    s = 0
    for i in range(k):
        s = s + A[i]

    return s


def quick_sort(A, l=0, h=None):
    if h is None:
        h = len(A) - 1

    if l < h:
        p = partition(A, l, h)
        quick_sort(A, l, p - 1)
        quick_sort(A, p + 1, h)


def partition(A, l, h):
    m = np.random.randint(l, h+1, dtype=int)

    A[h], A[m] = A[m], A[h]

    q = l
    for j in range(l, h):
        if A[j] <= A[h]:
            A[q], A[j] = A[j], A[q]
            q += 1

    A[q], A[h] = A[h], A[q]

    return q


if __name__ == "__main__":
    A = [3, 8, 60, 1, 60]
    k = 3

    print(algo_x(A, k))
    print(better_x(A, k))
    print(better_x_partition(A, k))

    # Benchmark
    quadratic_durations = []
    nlogn_durations = []
    logn_durations = []

    inputs = []
    # Possible: not good for bencmarching, should be randomly increasing??
    for i in range(11, 1011):
        inputs.append((np.random.randint(0, 10000, size=i, dtype=int),
                      np.random.randint(1, 10, dtype=int)))

    errors = 0
    for inp in inputs:
        if (algo_x(inp[0], inp[1]) != better_x(inp[0], inp[1])) or (algo_x(inp[0], inp[1]) != better_x_partition(inp[0], inp[1])):
            print(inp[0], inp[1])
            print(algo_x(inp[0], inp[1]))
            print(better_x(inp[0], inp[1]))
            errors += 1
            print(f"Error {errors}")

    for inp in inputs:
        tStart = time.perf_counter()
        algo_x(
            inp[0], inp[1])
        tEnd = time.perf_counter()

        quadratic_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        better_x(
            inp[0], inp[1])
        tEnd = time.perf_counter()

        nlogn_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        better_x_partition(
            inp[0], inp[1])
        tEnd = time.perf_counter()

        logn_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 1000)]  # Range from 0 to 300 inclusive

    # Plot array1 and array2
    plt.plot(x, quadratic_durations, label='algo_x O(n^2)')
    # Seems worse than actual algo, analyze
    plt.plot(x, nlogn_durations, label='better_x O(n*log(n))')
    plt.plot(x, logn_durations, label='better_x_partition O(log(n))')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'algo_x vs better_x vs better_x_partition')

    plt.legend()
    plt.show()
