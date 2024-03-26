#!/usr/bin/python3
# Write a program that reads a text file from standard input and outputs
# all the lines in the input that have maximal length.

import os

# Time Complexity: O(n)
# We loop through the array of line once, then we print the list of longest
# words O(2n) => O(n)

# Space Complexity: O(n)
# We store a cache array of longest words

# path = input("Enter the path for a text file: ") # Uncomment to provide custom txt file
path = "./src/utils/data/maxlines.txt"  # Comment to provide custom txt file
file = open(path, "r")
characters = ""

while 1:
    # read by character
    char = file.read(1)
    if not char:
        break
    else:
        characters += char

file.close()


def maxlines(s):
    # Does not count for time complexity evaluation We assume they
    S = s.split("\n")
    # are passed in one after the other in the standard input

    C = []

    if len(S) == 0:
        print("File has no lines")
        return

    C.append(S[0])

    for i in range(1, len(S)):
        if len(S[i]) > len(C[0]):
            C = []
            C.append(S[i])
        elif len(S[i]) == len(C[0]):
            C.append(S[i])

    for i in range(len(C)):
        print(C[i])

    return


# Runs
maxlines(characters)
