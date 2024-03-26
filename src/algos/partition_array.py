#!/usr/bin/python3
# Partitions an array in place based on a pivot index element, if it is not provided
# it chooses a random element in the array. The partition divides the array into smaller
# or equal elements to the pivot, the pivot and greater elements than the pivot. Returns
# the final pivot index

import math
import random

# Time Complexity: O(n)
# We loop throught the array linearly

# Space Complexity: O(1)
# We store only a few integers


def partition_array(A, begin=0, end=None):
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


if __name__ == '__main__':
    A = input("Enter numbers separated by spaces: ")
    A = A.split()
    A = [int(n) for n in A]

    p = None
    pString = input(
        "Enter partition pivot index (return to choose at random): ")
    if pString != "":
        p = int(pi)

    partition_array(A, p)
    print(A)
