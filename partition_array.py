#!/usr/bin/python3
# Partitions an array in place based on a pivot index element, if it is not provided
# it chooses a random element in the array. The partition divides the array into smaller
# or equal elements to the pivot, the pivot and greater elements than the pivot

import math
import random

# Time Complexity: O(n)
# We loop throught the array linearly

# Space Complexity: O(1)
# We store only a few integers


A = input("Enter numbers separated by spaces: ")
A = A.split()
A = [int(n) for n in A]

p = None
pString = input("Enter partition pivot index (return to choose at random): ")
if pString != "":
    p = int(pi)


def partition_array(A, pI=None):
    if pI == None:
        pI = math.floor(random.random() * len(A))
        print("Random index of: "+str(pI))
        print("Of value: "+str(A[pI]))

    A[pI], A[len(A) - 1] = A[len(A) - 1], A[pI]

    q = 0
    for i in range(len(A)):
        if A[i] <= A[-1]:
            A[q], A[i] = A[i], A[q]
            q = q + 1

    A[q], A[len(A) - 1] = A[len(A) - 1], A[q]


partition_array(A, p)
print(A)
