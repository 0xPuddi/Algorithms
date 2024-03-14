#!/usr/bin/python3
# MinMax:
# Write a program that reads a sequence of numbers from the standard input
# that are ordered with a single peak, return that peak. Example:
# 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1 returns 8
# 1 2 3 4 5 6 7 8 7 returns 8

# Time Complexity: O(n)
# It runs over each list element.

# Space Complexity: O(1)
# Creates one variable


A = input("Enter numbers separated by spaces: ")
A = A.split()
A = [int(n) for n in A]


def peak_sequential(A):
    n = None

    for i in range(1, len(A)):
        if i == len(A) - 1:
            n = A[i]
            break

        if A[i-1] > A[i]:
            n = A[i-1]
            break

    return n


# Time Complexity: O(log(n))
# It does a binary search

# Space Complexity: O(1)
# Creates one variables


def peak_binary_search(A):
    pivot = len(A) // 2

    def recurse(A, p, m):
        # Leftmost
        if (p == 0 and A[p] > A[p+1]):
            return A[p]

        # Rightmost
        if (p == len(A) - 1 and A[p - 1] < A[p]):
            return A[p]

        # Arbitrary
        if (A[p - 1] < A[p] and A[p] > A[p + 1]):
            return A[p]

        # Bisect right
        if A[p] < A[p + 1]:
            return recurse(A, (p + m) // 2, m)

        # Bisect left
        if A[p - 1] > A[p]:
            return recurse(A, p // 2, p)

    return recurse(A, pivot, len(A))


# Time Complexity: O(log(n))
# It does a binary search

# Space Complexity: O(1)
# Creates one variables


def peak_binary_search_light(A):
    pivot = len(A) // 2

    def recurse(A, p, m):
        # Leftmost
        if (p == 0):
            return A[p]

        # Rightmost
        if (p == len(A) - 1):
            return A[p]

        # Arbitrary
        if (A[p - 1] < A[p] and A[p] > A[p + 1]):
            return A[p]

        # Bisect right
        if A[p] < A[p + 1]:
            return recurse(A, (p + m) // 2, m)

        # Bisect left
        if A[p - 1] > A[p]:
            return recurse(A, p // 2, p)

    return recurse(A, pivot, len(A))


# Runs
print(peak_sequential(A))
print(peak_binary_search(A))
print(peak_binary_search_light(A))
