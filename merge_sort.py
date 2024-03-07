#!/usr/bin/python3
# Merge sort is a recursive algorithm that continuously splits the array
# in half until it cannot be further divided i.e., the array has only one
# element left (an array with one element is always sorted). Then the sorted
# subarrays are merged into one sorted array.

from merge_ordered import merge

# Time Complexity: O(n*log(n))
# It always divides the array into two halves and takes linear time to
# merge two halves.

# Space Complexity: O(n)
# All elements are stored in R and L arrays


A = input("Enter numbers separated by spaces: ")
A = A.split()
A = [int(n) for n in A]


def merge_sort(A):
    if len(A) > 1:
        pivot = len(A) // 2

        R = A[pivot:]
        L = A[:pivot]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            A[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            A[k] = R[j]
            j += 1
            k += 1

    return A


def merge_sort_merge_ordered(A):
    if len(A) == 1:
        return A

    m = len(A) // 2

    Al = merge_sort_merge_ordered(A[m:])
    Ar = merge_sort_merge_ordered(A[:m])

    return merge(Al, Ar)


# Runs
print(merge_sort(A))
print(merge_sort_merge_ordered(A))
