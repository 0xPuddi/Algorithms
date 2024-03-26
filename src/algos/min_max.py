#!/usr/bin/python3
# MinMax:
# Write a program that reads a sequence of numbers from the standard input
# with one or more numbers per line, and prints the minimum and the maximum
# values in the list.

# Time Complexity: O(n)
# It runs over each list element.

# Space Complexity: O(1)
# Creates two variables

import sys

# No sys imports, no algo global variables
N = []
b = True
while b:
    n = input("Number")
    if n == "":
        b = False
        break
    s = n.split()

    for a in s:
        N.append(int(a))


def min_max(N):
    mn = None
    ma = None

    for i in range(len(N)):
        if i == 0 and i == len(N) - 1:
            return N[i], N[i]

        if i == 0 and i == len(N):
            return N[0], N[1] if N[0] < N[1] else N[1], N[0]

        if i == 0:
            mn = N[i]
            ma = N[i]

        if mn > N[i]:
            mn = N[i]

        if ma < N[i]:
            ma = N[i]

    return mn, ma


# Sys imports
A = []
for line in sys.stdin:
    for a in line.split():
        A.append(int(a))

minimum = None
maximum = None
for a in A:
    if minimum == None or minimum > a:
        minimum = a
    if maximum == None or maximum < a:
        maximum = a

print('min =', minimum)
print('max =', maximum)
