#!/usr/bin/python3
# Histogram:
# Write a program that reads a list of non-negative numbers from the standard input,
# with one number per line, and prints a histogram corresponding to those numbers.
# In this histogram, each number x is represented by a line of x characters “#”.

import sys

# Time Complexity: O(n^2)
# It loops once for each element in the list, and it loops n times for each element

# Space Complexity: O(n)
# It uses the list passed in or O(1) since it does not make any new variable?


A = input("Enter numbers separated by spaces: ")
A = A.split()
A = [int(n) for n in A]


def histogram(N):
    for i in range(len(N)):
        for j in range(N[i]):
            sys.stdout.write("#")
        sys.stdout.write("\n")


# Runs
histogram(A)
