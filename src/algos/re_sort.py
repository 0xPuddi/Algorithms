# An array A of n numbers is sorted. Some elements are
# then set to 0. Write an algorithm Re-Sort(A) that takes
# such an array A and sorts it in-place and in time O(n).

import numpy as np
import time
import matplotlib.pyplot as plt
from src.algos.quick_sort import quick_sort
from random import shuffle


def re_sort(A):
    if len(A) == 0:
        return

    l = 0
    c = 0

    def find_next_zero():
        nonlocal A, l, c
        while l < len(A) and A[l] != 0:
            l += 1

        if c <= l:
            c = l + 1

    find_next_zero()
    while c < len(A):
        if A[c] != 0:
            A[l], A[c] = A[c], A[l]
            l += 1
            find_next_zero()
            continue

        c += 1

    for i in range(c - l):
        A.pop()


def linear(A):
    for i in range(len(A)):
        i = i


def nlogn(A):
    quick_sort(A)


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    for j in range(len(A) // 3):
        ri = np.random.randint(0, len(A) - 1, dtype=int)
        A[ri] = 0

    print(A)
    re_sort(A)
    print(A)

    # Benchmark
    durations = []
    linear_durations = []
    nlogn_durations = []

    inputs = []
    for i in range(0, 1000):
        A = []
        for j in range(i):
            ri = np.random.randint(0, 10, dtype=int)

            if ri % 2 == 0:
                A.append(0)
            else:
                A.append(j)

        inputs.append(A)

    quick_inputs = inputs
    for inp in quick_inputs:
        shuffle(inp)
        tStart = time.perf_counter()
        nlogn(inp)
        tEnd = time.perf_counter()

        nlogn_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        linear(inp)
        tEnd = time.perf_counter()

        linear_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        re_sort(inp)
        tEnd = time.perf_counter()

        durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 1000)]  # Range from 0 to 300 inclusive

    # Plot array1 and array2
    plt.plot(x, durations, label='re_sort O(n)')
    plt.plot(x, linear_durations, label='linear O(n)')
    plt.plot(x, nlogn_durations, label='nlogn O(n*log(n))')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        're_sort')

    plt.legend()
    plt.show()
