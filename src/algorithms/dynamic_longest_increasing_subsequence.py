

# Given an array of numbers nums, return the length of
# the longest strictly increasing subsequence

import random
import time
import numpy as np
import matplotlib.pyplot as plt


# Time Complexity: O(2^n)
def recursive_longest_increasing_subsequence(arr):
    maximum = 1
    n = len(arr)

    # To make use of recursive calls, this function must return
    # two things:
    # 1) Length of LIS ending with element arr[n-1]. We use
    # max_ending_here for this purpose
    # 2) Overall maximum as the LIS may end with an element
    # before arr[n-1] max_ref is used this purpose.
    # The value of LIS of full array of size n is stored in
    # *max_ref which is our final result
    def _recursive_longest_increasing_subsequence(arr, n):
        nonlocal maximum

        # Base Case
        if n == 1:
            return 1

        # maxEndingHere is the length of LIS ending with arr[n-1]
        maxEndingHere = 1

        # Recursively get all LIS ending with
        # arr[0], arr[1]..arr[n-2]
        # If arr[i-1] is smaller than arr[n-1], and
        # max ending with arr[n-1] needs to be updated,
        # then update it
        for i in range(1, n):
            res = _recursive_longest_increasing_subsequence(arr, i)
            if arr[i-1] < arr[n-1] and res+1 > maxEndingHere:
                maxEndingHere = res + 1

        # Compare maxEndingHere with overall maximum. And
        # update the overall maximum if needed
        maximum = max(maximum, maxEndingHere)

        return maxEndingHere

    # The function _lis() stores its result in maximum
    _recursive_longest_increasing_subsequence(arr, n)

    return maximum


# Time Complexity: O(n^2)
def dynamic_longest_increasing_subsequence(nums):
    LIS = [1] * len(nums)

    for i in range(len(nums) - 1, -1, -1):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1 + LIS[j])

    m = LIS[0]
    for i in range(len(LIS)):
        if LIS[i] > m:
            m = LIS[i]

    return m


# Time complexity: O(n^2)
def iterative_longest_increasing_subsequence(nums):
    acc = 0
    for i in range(len(nums)):
        t = 1  # We already have an element
        p = nums[i]

        if len(nums) - 1 - i <= acc:
            break

        for j in range(i + 1, len(nums)):
            if p < nums[j]:
                p = nums[j]
                t = t + 1

        if t > acc:
            acc = t

    return acc


if __name__ == "__main__":
    # S = input("Insert numbers separated by spaces: ")

    # A = []
    # for n in S.split(" "):
    #     A.append(int(n))

    A = [10, 9, 2, 5, 3, 7, 101, 18]

    print(dynamic_longest_increasing_subsequence(A))
    print(iterative_longest_increasing_subsequence(A))
    print(recursive_longest_increasing_subsequence(A))

    # Benchmark
    dynamic_durations = []
    iterative_durations = []
    recursive_durations = []

    inputs = []
    for i in range(1, 21):
        inputs.append(np.random.randint(0, 10000, size=i, dtype=int))

    for inp in inputs:
        tStart = time.perf_counter()
        dynamic_longest_increasing_subsequence(inp)
        tEnd = time.perf_counter()

        dynamic_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        iterative_longest_increasing_subsequence(inp)
        tEnd = time.perf_counter()

        iterative_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        recursive_longest_increasing_subsequence(inp)
        tEnd = time.perf_counter()

        recursive_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 20)]  # Range from 0 to 300 inclusive

    # Plot array1 and array2
    plt.plot(x, dynamic_durations, label='Dynamic O(n^2)')
    plt.plot(x, iterative_durations, label='Iterative O(n^2)')
    plt.plot(x, recursive_durations, label='Recursive O(2^n)')

    plt.yscale("log")
    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'Longest Increasing Subsequence: Dynamiv vs Iterative Time Complexity')

    plt.legend()
    plt.show()
