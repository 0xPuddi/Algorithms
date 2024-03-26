#!/usr/bin/python3
# Write a program that reads nine lines from the input each containing
# nine numbers between 1 and 9, representing a sudoku puzzle. The program
# should output Correct if the input represents a valid sudoku.

import os

# Time Complexity: O(n^2)
# we traverse the whole matrix both horizontally and verically two times,
# thus O(n^2 + n^2) = O(n^2)

# Space Complexity: O(1)
# We use only four variables, two bools and two integers.

A = []
for i in range(9):
    inp = input(f"Enter sudoku line number {i+1}: ")
    inp = inp.split()
    inp = [int(n) for n in inp]
    A.append(inp)


def check_sudoku(N):
    n_row = 0
    error_row = False
    for i in range(len(N)):
        result = 0

        for j in range(len(N[i])):
            result += N[i][j]

            if j == len(N[i]) - 1 and result != 45:
                error = True
                err_row = i

    n_col = 0
    error_col = False
    for i in range(len(N)):
        result = 0

        for j in range(len(N)):
            result += N[j][i]

            if j == len(N) - 1 and result != 45:
                error_col = True
                n_col = i

    if error_row:
        print("Incorrect, row error: "+str(n_row))
    elif error_col:
        print("Incorrect, column error: "+str(n_col))
    else:
        print("Correct")

    return


# Runs
check_sudoku(Z)
