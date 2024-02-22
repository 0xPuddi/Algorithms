#!/usr/bin/python3
# Sieve of Eratosthenes algo:
# Write a function that takes an integer n and returns a list,
# based on the index, of Trues for prime numbers and False
# for anything else starting from 2 (1 and 0 are false).

# Time Complexity: n*log(n)
# It runs for every element less than n and for each p that is
# a prime number it loops n/p times.

# Space Complexity: n
# It uses a varible and a list of bools that grows linearly with
# the input.

# sieve implemented with for loop
def sieve(n):
    A = [True]*(n + 1)
    A[0] = False
    A[1] = False
    p = 2

    while p <= n:
        if A[p]:
            for i in range(2*p, n+1, p):
                A[i] = False
        p += 1
    return A


# sieve2 implemented with while loop
def sieve2(n):
    A = [True]*(n + 1)
    A[0] = False
    A[1] = False
    p = 2

    while p <= n:
        if A[p]:
            i = p + p
            while i <= n:
                A[i] = False
                i += p
        p += 1
    return A


# Runs
print(sieve(10))
print(sieve2(10))
