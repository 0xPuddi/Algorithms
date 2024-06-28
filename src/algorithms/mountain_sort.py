
import math
import random


def mountain_sort(A):
    m = A[0]
    mIndex = 0

    for i in range(1, len(A)):
        if A[i] > m:
            m = A[i]
            mIndex = i

    middle = len(A) // 2
    A[middle], A[mIndex] = A[mIndex], A[middle]

    quicksort_increasing(A, 0, middle - 1)
    quicksort_decreasing(A, middle + 1, len(A) - 1)


def quicksort_increasing(A, start, end):
    if start < end:
        q = sb_partition_array(A, start, end)
        quicksort_increasing(A, start, q - 1)
        quicksort_increasing(A, q + 1, end)


def sb_partition_array(A, start, end):
    q = start

    for i in range(start, end):
        if A[i] <= A[end]:
            A[q], A[i] = A[i], A[q]
            q = q + 1

    A[q], A[end] = A[end], A[q]

    return q


def quicksort_decreasing(A, start, end):
    if start < end:
        q = bigger_smaller_partition(A, start, end)
        quicksort_decreasing(A, start, q - 1)
        quicksort_decreasing(A, q + 1, end)


def bigger_smaller_partition(A, start, end):
    q = start

    for i in range(start, end):
        if A[i] >= A[end]:
            A[q], A[i] = A[i], A[q]
            q = q + 1

    A[q], A[end] = A[end], A[q]

    return q


if __name__ == "__main__":
    A = [8, 2, 5, -12, 2, 11, -15, -8, -1, 12]
    mountain_sort(A)
    print(A)
