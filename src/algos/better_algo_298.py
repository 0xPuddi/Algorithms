

import numpy as np
import matplotlib.pyplot as plt
import time
from src.algos.merge_sort import merge_sort

# The algorithm chekcks whether there are at least 3 different numbers in the input list


# Complexity O(n*log(n))
def algo_x(A):
    B = merge_sort(A)
    n = len(A)
    x = 1

    for i in range(1, n):
        if B[i] != B[i - 1]:
            x = x + 1

    if x > 3:
        return True
    else:
        return False


# Complexity O(n)
def better_x(A):
    x = 0

    for i in range(1, len(A)):
        if A[i - 1] != A[i]:
            x += 1

    if x >= 3:
        return True

    return False


if __name__ == "__main__":
    A = [4, 4, 4, 4, 2, 4, 5, 6, 4, 4, 4, 4]

    print(algo_x(A))
    print(better_x(A))

    # Benchmark
    quartic_durations = []
    cubic_durations = []

    inputs = []
    # Possible: not good for bencmarching, should be randomly increasing??
    for i in range(1, 51):
        inputs.append(np.random.randint(0, 10000, size=i, dtype=int))

    errors = 0
    for inp in inputs:
        if algo_x(inp) != better_x(inp):
            errors += 1
            print(f"Error {errors}")

    for inp in inputs:
        tStart = time.perf_counter()
        algo_x(
            inp)
        tEnd = time.perf_counter()

        quartic_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        better_x(
            inp)
        tEnd = time.perf_counter()

        cubic_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 50)]  # Range from 0 to 300 inclusive

    # Plot array1 and array2
    plt.plot(x, quartic_durations, label='algo_x O(n*log(n))')
    plt.plot(x, cubic_durations, label='better_x O(n)')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'algo_x vs better_x')

    plt.legend()
    plt.show()
