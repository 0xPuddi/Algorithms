

# Given an integer array nums and an integer k, return the kth
# largest element in the array


import random
import time
import numpy as np
import matplotlib.pyplot as plt
import math


# Quick Select
# Time complexity: O(n)
# Space complexity: O(n)
def kth_largest_element_quick(nums, k):
    if len(nums) == 0:
        return

    pivot = random.choice(nums)
    left = [x for x in nums if x > pivot]
    mid = [x for x in nums if x == pivot]
    right = [x for x in nums if x < pivot]

    L, M = len(left), len(mid)

    if k <= L:
        return kth_largest_element_quick(left, k)
    elif k > L + M:
        return kth_largest_element_quick(right, k - L - M)
    else:
        return mid[0]


# Quick Select In-Place, it will suffke the original array, but
# since it wasn't ordered it shouldnt be a concerne
# Time complexity: O(n)
# Space complexity: O(1)
def kth_largest_element_quick_inplace(nums, k):
    k = len(nums) - k

    if len(nums) == 0:
        return

    def partition(A, begin=0, end=None):
        if end == None:
            end = len(A) - 1

        pI = begin + math.floor(random.random() * (end - begin))
        A[pI], A[end] = A[end], A[pI]

        q = begin
        for i in range(begin, end):
            if A[i] <= A[end]:
                A[q], A[i] = A[i], A[q]
                q = q + 1

        A[q], A[end] = A[end], A[q]

        return q

    mid = partition(nums, 0, len(nums) - 1)

    while mid != k:

        if k <= mid:
            mid = partition(nums, 0, mid - 1)
            continue
        elif k > mid:
            mid = partition(nums, mid + 1, len(nums) - 1)
            continue

    return nums[mid]


# Time complexity: O(nlog(k))
# Space complexity: O(k)
# A max heap can't be used because, for example if we have k = 3
# and there are already two elements i the heap, once we add the
# third, even if it is the correct kth element, it will stay in
# place third as the heap allows it, and it will then be popped
# off from the heap
def kth_largest_element_heap(nums, k):
    if len(nums) == 0 or len(nums) < k:
        return

    min_heap = []

    def min_heapify(root):
        nonlocal min_heap

        while True:
            l = root * 2 + 1
            r = root * 2 + 2

            m = root
            if l < len(min_heap) and min_heap[m] > min_heap[l]:
                m = l
            if r < len(min_heap) and min_heap[m] > min_heap[r]:
                m = r

            if m == root:
                return

            min_heap[m], min_heap[root] = min_heap[root], min_heap[m]

            root = m

    def min_heap_push(el):
        nonlocal min_heap

        if len(min_heap) == 0:
            min_heap.append(el)
            return

        i = (len(min_heap) - 1) // 2
        min_heap.append(el)
        while True:
            min_heapify(i)

            if i == 0:
                return

            i = i // 2

    def min_heap_pop():
        nonlocal min_heap

        if len(min_heap) == 0:
            return

        el = min_heap[0]
        min_heap[0] = min_heap[-1]
        min_heap.pop()

        min_heapify(0)

        return el

    for n in nums:
        min_heap_push(n)

        if len(min_heap) > k:
            min_heap_pop()

    return min_heap[0]


# Time complexity: O(n^k)
# Space complexity: O(1)
def kth_largest_element_sort(nums, k):
    if len(nums) == 0 or len(nums) < k:
        return

    nums.sort()

    return nums[-k]


# Time complexity: O(n^k)
# Space complexity: O(1)
def kth_largest_element_exp(nums, k):
    if len(nums) == 0 or len(nums) < k:
        return

    last = nums[0]
    for n in nums:
        if last <= n:
            last = n
    k = k - 1

    while k > 0:
        acc = nums[0]

        for n in nums:
            if n != last and n <= last and n >= acc:
                acc = n

        last = acc
        k = k - 1

    return last


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7, 8, 88, 3, 4, 5, 6, 7, 9, 100]
    k = 2

    print(kth_largest_element_sort(A, k))
    print(kth_largest_element_exp(A, k))
    print(kth_largest_element_heap(A, k))
    print(kth_largest_element_quick(A, k))
    print(kth_largest_element_quick_inplace(A, k))

    # Benchmark
    exp_durations = []
    sort_durations = []
    heap_durations = []
    quick_durations = []
    quick_inplace_durations = []

    inputs = []
    for i in range(1, 121):
        inputs.append((np.random.randint(0, 10000, size=i, dtype=int),
                      np.random.randint(1, i+1, size=1, dtype=int)))

    for inp in inputs:
        tStart = time.perf_counter()
        kth_largest_element_exp(inp[0], inp[1])
        tEnd = time.perf_counter()

        exp_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        kth_largest_element_sort(inp[0], inp[1])
        tEnd = time.perf_counter()

        sort_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        kth_largest_element_heap(inp[0], inp[1])
        tEnd = time.perf_counter()

        heap_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        kth_largest_element_quick(inp[0], inp[1])
        tEnd = time.perf_counter()

        quick_durations.append((tEnd - tStart) * 1_000_000)

    for inp in inputs:
        tStart = time.perf_counter()
        kth_largest_element_quick_inplace(inp[0], inp[1])
        tEnd = time.perf_counter()

        quick_inplace_durations.append((tEnd - tStart) * 1_000_000)

    x = [i for i in range(0, 120)]  # Range from 0 to 1000

    # Plot array1 and array2
    plt.plot(x, exp_durations, label='Exp')
    plt.plot(x, sort_durations, label='Sort')
    plt.plot(x, heap_durations, label='heap')
    plt.plot(x, quick_durations, label='Quick')
    plt.plot(x, quick_inplace_durations, label='Quick_InPlace')

    plt.xlabel('Input Size')
    plt.ylabel('Time')
    plt.title(
        'lol')

    plt.yscale("log")
    plt.legend()
    plt.show()
