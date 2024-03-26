#!/usr/bin/python3
# QuickSort is an in place sorting algorithm based on the Divide and Conquer
# algorithm that picks an element as a pivot and partitions the given array
# around the picked pivot by placing the pivot in its correct position in the
# sorted array.

from partition_array import partition_array
import random

# Worse Time Complexity: O(n^2)
# At worse, pick always the boundary element, thus reducing the array into
# n - 1 each time

# Median Time Complexity: O(n*log(n))
# At average, we pick the 25% or 75% element of the partitioned array (best is
# middle, thus 50%), dividing then the array into 1/4 and 3/4 each iteration

# Best Time Complexity: O(n*log(n))
# At best, we will always split the array in two subarrays and order them
# linearly.

# Space Complexity: O(1)
# We store only a few integers


A = input("Enter numbers separated by spaces: ")
A = A.split()
A = [int(n) for n in A]


def quick_sort(A, begin=0, end=None):
    if end == None:
        end = len(A) - 1

    if begin < end:
        pI = partition_array(A, begin, end)

        quick_sort(A, begin, end - 1)
        quick_sort(A, begin + 1, end)


quick_sort(A)
print(A)
