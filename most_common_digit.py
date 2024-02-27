#!/usr/bin/python3
# Most Common Digit:
# Write a function called most_common_digit(n) that takes an integer n,
# and returns the most common digit in the decimal representation of n.
# If there are two or more most common digits, the function must return
# the smallest one.

inp = input("Inster an integer digit: ")


# Time Complexity: O(n)
# We loop lineraly through the input three times, thus O(3n) = O(n)

# Space Complexity: O(n)
# We store two arrays and a dictionary that can be as wide as the input,
# thus O(3n) = O(n)

# Dictionary
# No sorting allowed
def most_commond_digit_dict(n):
    D = {}
    C = []
    I = []

    # Divide the integer in its single digits
    spl = str(n)
    for i in range(len(spl)):
        I.append(int(spl[i]))

    # Loop through the digits and update dictionary while mantaining a
    # cache array of most common values
    D[I[0]] = 1
    C.append(D[I[0]])
    for i in range(1, len(I)):
        digit = I[i]
        if digit in D:
            D[digit] += 1
        else:
            D[digit] = 1

        if D[C[0]] < D[digit]:
            C = []
            C.append(digit)
        elif D[C[0]] == D[digit]:
            C.append(digit)

    # Loop through all common values and return the smallest one
    c = C[0]
    for i in range(len(C)):
        if C[i] <= c:
            c = C[i]

    print(c)

    return


# Time Complexity: O(n^2)
# We loop through the array and reloop the rest from the first loop index
# to the length of the array, and loop one time over the array and one time
# over the integer input, thus O((n(n+1))/2 +2n) = O(n^2)

# Space Complexity: O(n)
# We store two arrays that can be as wide as the input, thus O(2n) = O(n)

# No Dictionary, only: int, array, tuple or strings
# Only pop operations allowed
# No sorting allowed
def most_commond_digit(n):
    # Divide the integer in its single digits
    I = []
    spl = str(n)
    for i in range(len(spl)):
        I.append(int(spl[i]))

    # Loop through all digit and for each one count it
    C = []
    escape = "#"
    for i in range(len(I)):
        if I[i] == escape:
            continue

        f = []
        f.append(I[i])
        f.append(0)

        for j in range(i + 1, len(I)):
            if I[j] == escape and j != len(I):
                continue

            if I[i] == I[j]:
                f[1] += 1
                I[j] = escape

            if j == len(I) - 1:
                C.append(f)

    # Print the least most common digit
    c = C[0]
    for i in range(1, len(C)):
        if c[1] < C[i][1]:
            c = C[i]
        elif c[1] == C[i][1] and c[0] > C[i][0]:
            c = C[i]

    return


most_commond_digit_dict(inp)
most_commond_digit(int(inp))
