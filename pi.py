#!/usr/bin/python3
# Pi:
#  Write a program that reads a positive integer N as a command-line argument
#  and prints the value of the function pi(i) for every positive i < N, where
# pi(i) is the number of prime numbers that are less than or equal to i.

import sys

# Time Complexity: O(nlog(n))
# It uses Sieve of Ratosthenes complexity, and loops over the list one more time
# still 2n is approximated to n

# Space Complexity: O(n)
# It uses a list of booleans and a single variable, thus n + 1 = n


# we implement the sieve of Eratosthenes
def sieve_of_ratosthenes(n):
    P = [True]*n
    P[0] = False
    P[1] = False
    i = 0

    while i < n:
        if P[i]:
            p = 2*i

            while p < n:
                P[p] = False
                p += i
        i += 1

    return P


# pi count
def pi(n):
    counter = 0
    P = sieve_of_ratosthenes(n+1)

    for j in range(1, n+1):
        if P[j]:
            counter += 1
        print(j, counter)


# One function, same as the one above but it skips 2 and 3 when looping for
# primes
def pi(n):
    # we implement the sieve of Eratosthenes
    S = [True]*(n + 1)
    S[0] = False
    S[1] = False
    p = 2
    while p * p <= n:
        if S[p]:
            i = p * p
            while i <= n:
                S[i] = False
                i = i + p
        p = p + 1

    # pi count
    count = 0
    i = 1
    while i <= n:
        if S[i]:
            count = count + 1
        print(i, count)
        i = i + 1


# Runs
pi(11)
