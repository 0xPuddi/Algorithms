#!/usr/bin/python3
# Write a program that reads a list of numbers n from the standard input,
# with one or more numbers per line, and prints a vertical histogram corresponding
# to those numbers. In this histogram, each number x is represented by a
# column of x characters # starting from a base-line of n dash characters
# - representing value 0. Positive numbers are represented by a column above zero
# while negative numbers are represented with a column below zero.

# Time Complexity: O(n^2)
# We are looping over the array once, so n then we are looping twice: from the lowest
# value to the biggest value and over each element of the list, thus n + 2n^2, then we
# approximate constant values and to the biggest magnitude

# Space Complexity: O(1)
# We are using only few variables


A = input("Enter numbers separated by spaces: ")
A = A.split()
A = [int(n) for n in A]


# First version
def vertical_histogram(A):
    # Find the bigger and smaller element
    b = A[0]
    s = A[0]
    for i in range(1, len(A)):
        if A[i] >= b:
            b = A[i]
        if A[i] <= s:
            s = A[i]

    # Run throught the array and print each element
    # bookeep with b and s

    # Print over
    bi = 0
    _b = b
    while bi < b:
        for j in range(len(A)):
            if A[j] == _b:
                A[j] -= 1
                print("#", end="")
            else:
                print(" ", end="")

        _b -= 1
        bi += 1
        print()

    # Print col
    for j in range(len(A)):
        print("-", end="")
    print()

    # Print under
    si = 0
    while si > s:
        for j in range(len(A)):
            if A[j] != 0:
                A[j] += 1
                print("#", end="")
            else:
                print(" ", end="")

        si -= 1
        print()


# Second version
def v_histogram(A):
    top = 0
    bottom = 0
    for a in A:
        if a > top:
            top = a
        elif a < bottom:
            bottom = a

    i = top
    while i > 0:
        for a in A:
            if a >= i:
                print('#', end='')
            else:
                print(' ', end='')
        print()
        i = i - 1

    for a in A:
        print('-', end='')
    print()
    while i > bottom:
        i = i - 1
        for a in A:
            if a <= i:
                print('#', end='')
            else:
                print(' ', end='')
        print()


# Runs
vertical_histogram(A)
print("\n")
v_histogram(A)
