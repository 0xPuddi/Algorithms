#!/usr/bin/python3
# Write a function that takes an array of integers and returns the median of that array.
# Write it with a median complexity of O(n).

import random
import time
from merge_sort import merge_sort
import numpy as np
import matplotlib.pyplot as plt

# Worst Time Complexity: O(n^2)
# In the wors case the algorithm picks up a boundary element, which will reduce the
# array of one element each time, giving us a complexity of O(n + n - 1 + n -2 + ...),
# which can be described as O((n(n-1))/2) = O(n^2).

# Median Time Complexity: O(n)
# Since the algorithm works with a random selection medially the input that needs
# to be traversed linearly is splitted each time, giving us a complexity of
# O(n + n/2 + n/4 + n/8 + ...), which is appproximated to O(n).

# Space Complexity: O(n)
# We store three arrays that are as big as the input array.


# k is the position that we are looking for
def selection(A, k):
    L = []
    M = []
    R = []

    v = random.choice(A)

    for e in A:
        if e < v:
            L.append(e)
        elif e > v:
            R.append(e)
        if e == v:
            M.append(e)

    if k < len(L):
        return selection(L, k)
    if k >= len(L) + len(M):
        return selection(R, k - (len(L) + len(M)))
    else:
        return v


def median(A):
    return selection(A, len(A) // 2)


# Time Complexity: O(n)
# Merge sort time complexity

# Space Complexity: O(n)
# Merge sort space complexity


def median_ordered(A):
    A = merge_sort(A)
    return A[len(A) // 2]


# We run a benchmark between median and median ordered to demonstrate that an algorithm
# with a median time complexity better than an absolute complexity of another algorithm,
# even if the better median time has a worse worst case complexity is still a better choice
if __name__ == '__main__':
    A = input("Enter numbers separated by spaces: ")
    A = A.split()
    A = [int(n) for n in A]

    print(median(A))
    print(median_ordered(A))

    # Benchmark
    median_durations = []
    median_ordered_durations = []

    inputs = []
    for i in range(1, 1001):
        inputs.append(np.random.randint(0, 10000, size=i, dtype=int))

    for inp in inputs:
        tStart = time.perf_counter()
        median(inp)
        tEnd = time.perf_counter()

        median_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        median_ordered(inp)
        tEnd = time.perf_counter()

        median_ordered_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 1000)]  # Range from 0 to 300 inclusive

    # Plot array1 and array2
    plt.plot(x, median_durations, label='Median')  # looks like log(n) -> why?
    plt.plot(x, median_ordered_durations, label='Median Ordered')

    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'Median: Median complexity of O(n) and Worse complexity of O(n^2)\nversus\nMedian Ordered: Absolute complexity of O(n*log(n))')

    plt.legend()
    plt.show()
