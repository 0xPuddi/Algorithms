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
x = int(input("Insert integer you wish to count less than: "))


def count_lower(A, x):
    c = 0

    for i in range(len(A)):
        if A[i] < x:
            c += 1

    print(c)


# Runs
count_lower(A, x)
