#!/usr/bin/python3
# To sort an array of size N in ascending order iterate over the array
# and compare the current element (key) to its predecessor, if the key
# element is smaller than its predecessor, compare it to the elements
# before. Move the greater elements one position up to make space for
# the swapped element.

import os

# Time Complexity: O(n^2)
# We run through the array once, and for the inner loop we run back the
# whole array for each element that is higher than the previous one.
# Thus O((n * (n - 1)) / 2) = O(n^2)

# Space Complexity: O(1)
# We store a few integers


array = input("Insert integers separated by spaces: ")
A = [int(n) for n in array.split(" ")]


def insertion_sort(A):
    for i in range(1, len(A)):
        if A[i - 1] <= A[i]:
            continue

        j = i
        while j > 0 and A[j - 1] > A[j]:
            A[j - 1], A[j] = A[j], A[j - 1]
            j -= 1

    return A


# Runs
print(insertion_sort(A))
