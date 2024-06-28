#!/usr/bin/python3
# Given an unordered sequence of integers A = a1, a2, ..., an, a maximal identical
# sequence is a sequence of adjacent identical values v = a1 = a2 = ... = ak of
# maximal length k. Write a program that reads an input sequence A, with one or more
# numbers per line, and outputs the value of the first (leftmost) maximal identical
# sequence in A.

# Time Complexity: O(n)
# We traverse the list once, thus O(n)

# Space Complexity: O(1)
# We store four variables: O(4), by approximating we get O(1)

A = input("Enter numbers separated by spaces: ")
A = A.split()
A = [int(n) for n in A]


def longest_identical_sequence(N):
    max_n = N[0]
    max_frequency = 1
    current_n = max_n
    current_frequency = max_frequency

    i = 1
    while i < len(N):
        if current_n == N[i]:
            current_frequency += 1
        else:
            if current_frequency > max_frequency:
                max_n = current_n
                max_frequency = current_frequency

            current_n = N[i]
            current_frequency = 1

        i += 1

    print(max_n)


longest_identical_sequence(A)
