# We want to cover a set of n numbers with a set of k intervals such that
# the total length of the intervals is minimal. An interval [a, b], defined
# by two numbers a ≤ b, covers all the numbers between a and b, including
# a and b. For example, [3, 7] and [6, 10.5] cover all the numbers in
# A = [3, 5, 7, 9]. However, their total length (7−3)+(10.5−6) = 8.5 is not
# minimal. The minimal length is instead 4. In general, we want to have k
# intervals [a1, b1], [a2, b2], . . . , [ak, bk] such that, for each number
# x in A, there is at least one interval [ai, bi] such that ai ≤ x ≤ bi, and
# the total length P (bi − ai) is minimal.
# Write an algorithm Minimal-K-Interval-Cover-Length(A, k) that, given an array
# A of numbers and a positive integer k, returns the minimal total length of k
# intervals that cover every number in A.
# Write an algorithm Minimal-K-Interval-Cover-Length(A, k) that runs in O(n log n)
# time.


import numpy as np
import time
import matplotlib.pyplot as plt
from src.algos.quick_sort import quick_sort


# Complexity: O(nlog(n))
def minimal_k_interval_cover_length(A: list[int], k: int) -> int:
    if k == len(A) or len(A) == 1 or k == 0:
        return 0

    Costs = []
    for i in range(1, len(A)):
        Costs.append(A[i] - A[i - 1])

    lb = 0
    hb = len(Costs) - 1
    p = partition(Costs, lb, hb)
    ik = len(Costs) - k
    while p != ik:
        # We partition for the necessary highest k values of the array
        if p < ik:
            lb = p + 1
        elif p > ik:
            hb = p - 1

        p = partition(Costs, lb, hb)

    k = k - 1
    for i in range(k):
        Costs.pop()

    print(Costs)

    # We calculate total cost
    tot_cost = 0
    for i in range(len(Costs)):
        tot_cost += Costs[i]

    return tot_cost


def linear(A):
    for i in range(len(A)):
        i = i
    return


def logn(A):
    if len(A) == 1:
        return

    v = np.random.randint(A[0], A[-1], dtype=int)

    lb = 0
    hb = len(A) - 1
    i = (lb + hb) // 2

    while v != A[i] and lb != hb:
        if A[i] < v:
            lb = i
        else:
            hb = i

        i = (lb + hb) // 2
        v = A[i]

    return


def nlogn(A):
    quick_sort(A)


def quadratic(A):
    for i in range(len(A)):
        for j in range(len(A)):
            i = i
    return


def partition(A, lb, hb):
    m = None
    if lb == hb + 1:
        m = lb
    else:
        m = np.random.randint(lb, hb + 1, dtype=int)

    A[m], A[hb] = A[hb], A[m]

    p = lb
    for j in range(lb, hb):
        if A[j] <= A[hb]:
            A[p], A[j] = A[j], A[p]
            p += 1

    A[hb], A[p] = A[p], A[hb]
    return p


if __name__ == "__main__":
    A = [4, 3, 13, 45, 33, 12, 66, 89, 90]
    A.sort()
    k = 3
    print(minimal_k_interval_cover_length(A, k))

    A = [3, 5, 7, 9]
    k = 2
    print(minimal_k_interval_cover_length(A, k))

    # Benchmark
    durations = []
    linear_durations = []
    logn_durations = []
    nlogn_durations = []
    quadratic_durations = []

    inputs = []
    # Possible: not good for bencmarching, should be randomly increasing??
    for i in range(1, 5001):
        inputs.append((np.random.randint(0, 10000, size=i,
                      dtype=int), np.random.randint(0, i, dtype=int)))

    for inp in inputs:
        tStart = time.perf_counter()
        nlogn(
            inp[0])
        tEnd = time.perf_counter()

        nlogn_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        minimal_k_interval_cover_length(
            inp[0], inp[1])
        tEnd = time.perf_counter()

        durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        linear(
            inp[0])
        tEnd = time.perf_counter()

        linear_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        logn(
            inp[0])
        tEnd = time.perf_counter()

        logn_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        quadratic(
            inp[0])
        tEnd = time.perf_counter()

        quadratic_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 5000)]  # Range from 0 to 300 inclusive

    average_over_n = 21
    durations_average = [0] * average_over_n
    for i in range(average_over_n, len(durations)):
        durations_average.append(0)

        for j in range(i, i - (average_over_n + 1), -1):
            durations_average[-1] += durations[j]

        durations_average[-1] = (durations_average[-1] / 10)

    # Plot array1 and array2
    plt.plot(x, durations, label='minimal_k_interval_cover_length O(log(n))')
    plt.plot(x, durations_average,
             label='minimal_k_interval_cover_length moving average')
    plt.plot(x, nlogn_durations, label='quick_sort O(nlog(n))')
    plt.plot(x, logn_durations, label='log O(log(n))')
    plt.plot(x, linear_durations, label='linear O(n)')
    plt.plot(x, quadratic_durations, label='quadratic O(n^2)')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'minimal_k_interval_cover_length')

    plt.legend()
    plt.show()
