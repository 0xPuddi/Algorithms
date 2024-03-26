#!/usr/bin/python3
# Take two arrays of binary numbers of equal length from most significant digit
# to least significant digit, sum them and return an array of summed binary digits

# Time Complexity: O(n)
# We run once linearly an at the same time through both bits array

# Space Complexity: O(n)
# We store an array of bits

# Returns a pair (s, c)
def full_adder(a, b, c):
    sm = a ^ b
    rest = (a & b) | (a & c) | (b & c)

    return (sm ^ c, rest)


def binary_addition(A, B):
    c = 0
    i = j = 0
    R = []

    while i < len(A) or j < len(B) or c == 1:
        a = 0
        b = 0

        if i < len(A):
            a = A[i]
        if j < len(B):
            b = B[j]

        sm, rest = full_adder(a, b, c)

        R.append(sm)
        c = rest

        i += 1
        j += 1

    return R


print(binary_addition([1, 1, 1], [1, 1, 0]))
