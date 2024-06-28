#!/usr/bin/python3
# Three-way-partition: Write an in-place partition that will divide
# the array based on a pivot into three parts: element smaller then
# the piot, element equal to the pivot and elements greater then the
# pivot. Return the indexes of the boundaries of the section equal to
# the pivot.

import math
import random


# Time Complexity: O(n)
# We traverse linearly the array

# Space Complexity: O(1)
# We partition in-place storing a few indexes


arr = [3, 1, 9, 1, 5, 4, 2, 6, 5, 3, 5]
pivot = 5
A = [1, 4, 2, 4, 2, 4, 1, 2, 4, 2, 2, 2, 2, 2, 4, 1, 4, 4, 4]


def three_way_partition(A, begin, end):
    q_high = end
    q_low = begin

    iPivot = begin + math.floor(random.random() * (end - begin))
    pivot = A[iPivot]

    print("pivot is: ", pivot)

    i = begin
    while i <= q_high:
        if A[i] < pivot:
            A[q_low], A[i] = A[i], A[q_low]
            q_low += 1
            i = i + 1
        elif A[i] > pivot:
            A[q_high], A[i] = A[i], A[q_high]
            q_high -= 1
        else:
            i = i + 1

    return q_low, q_high


if __name__ == "__main__":
    print(three_way_partition(A, 0, len(A) - 1))
    print(A)
    print(three_way_partition(arr, 0, len(arr) - 1))
    print(arr)
