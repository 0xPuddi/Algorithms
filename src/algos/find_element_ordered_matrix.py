

# Given an m x n integer matrix with the following properties:
# Each row is sorted in non-decreasing order
# The first integer is greater than the last integer of the previous row
# Diven an integer return True if it is in the matrix or False otherwise

import random
import time
import numpy as np
import matplotlib.pyplot as plt


#
def find_element_matrix_binary_search(matrix: list[list[int]], target: int):
    m = len(matrix)
    n = len(matrix[0])

    L, R = 0, m*n - 1

    while L <= R:
        mid = (L+R) // 2
        # i is the index of the row
        # j is the index of the column
        i, j = mid // n, mid % n

        if target == matrix[i][j]:
            return True
        elif target < matrix[i][j]:
            R = mid - 1
        elif target > matrix[i][j]:
            L = mid + 1

    return False


def find_element_matrix_moving_search(matrix: list[list[int]], target: int):
    c = len(matrix[0]) - 1
    r = 0

    while c < len(matrix[0]) and r < len(matrix):
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            r += 1
        elif matrix[r][c] > target:
            c -= 1

    return False


def find_element_matrix_linear_search(matrix: list[list[int]], target: int):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == target:
                return True

    return False


if __name__ == "__main__":
    A = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    a = 3
    b = 24

    print(find_element_matrix_binary_search(A, a))
    print(find_element_matrix_binary_search(A, b))
    print(find_element_matrix_moving_search(A, a))
    print(find_element_matrix_moving_search(A, b))

    # Benchmark
    binary_durations = []
    moving_durations = []
    linear_durations = []

    inputs = []
    targets = []

    # Possible: not good for bencmarching, should be randomly increasing??
    for i in range(1, 1001):
        inputs.append([])
        t = 0
        for j in range(i):
            inputs[i - 1].append([])
            for k in range(i):
                inputs[i - 1][j].append(t)
                t = t + 1

    for i in range(1000):
        targets.append(np.random.randint(700, 1000, size=1, dtype=int))

    for inp in inputs:
        tStart = time.perf_counter()
        find_element_matrix_linear_search(
            inp, targets[np.random.randint(0, 999, size=1, dtype=int)[0]])
        tEnd = time.perf_counter()

        linear_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        find_element_matrix_binary_search(
            inp, targets[np.random.randint(0, 999, size=1, dtype=int)[0]])
        tEnd = time.perf_counter()

        binary_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        find_element_matrix_moving_search(
            inp, targets[np.random.randint(0, 999, size=1, dtype=int)[0]])
        tEnd = time.perf_counter()

        moving_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 1000)]  # Range from 0 to 300 inclusive

    # Plot array1 and array2
    plt.plot(x, binary_durations, label='Binary O(log(n x m))')
    plt.plot(x, moving_durations, label='Moving O(m + n)')
    plt.plot(x, linear_durations, label='Linear O(m*n)')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'Non-Decreasing Ordered Matrix Search: Binari VS Moving VS Linear')

    plt.legend()
    plt.show()
