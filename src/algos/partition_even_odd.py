#!/usr/bin/python3
# Write a function count_lower(A,x) that returns the number of elements
# in A whose value is less than x.

import os

# Time Complexity: O(n)
# We loop through the input array once

# Space Complexity: O(1)
# We only store an integer


array = input("Insert integers separated by spaces: ")
A = [int(n) for n in array.split(" ")]


# We take count of each odd number we encountered, which also give us the
# exact index of the first odd element if we subtract it to the current running
# index, then when we traverse the array and when encountering an even number
# we swap it with the first odd element.
def parttion_even_odd(P):
    odd_numbers = 0

    for i in range(len(P)):
        if P[i] % 2 == 1:
            odd_numbers += 1
        else:
            P[i-odd_numbers], P[i] = P[i], P[i-odd_numbers]

    print(P)


# We start with i at the first element of the array and j at the last
# then we increment i if it is pointing at a even number, and we decrease
# j if it is pointing at an odd number, at last if j is pointing at an
# even number we swap it to index i.
def parttion_even_odd_v2(A):
    i = 0
    j = len(A) - 1

    while i < j:
        if A[i] % 2 == 0:
            i += 1
        elif A[j] % 2 == 1:
            j -= 1

        else:
            A[j], A[i] = A[i], A[j]
            i += 1
            j -= 1

    print(A)


# We keep e to the first odd element
# We traverse f in the array and swap with e when we encounter
# an even number
def parttion_even_odd_v3(N):
    e = 0
    f = 0

    while f < len(N):
        if N[f] % 2 == 0:
            A[e], A[f] = A[f], A[e]
            e += 1

        f += 1

    print(N)


# Runs
parttion_even_odd(A)
parttion_even_odd_v2(A)
parttion_even_odd_v3(A)
