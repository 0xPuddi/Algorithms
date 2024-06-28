#!/usr/bin/python3
# Write a function remove_value_stable(A,x) that takes an array of numbers and a number
# and returns the array without all elements equalt to the number, mantaining list order

# Time Complexity: O(n)
# We run through the array once

# Space Complexity: O(1)
# We store only to integers


array = input("Insert integers separated by spaces: ")
A = [int(n) for n in array.split(" ")]
x = int(input("Insert integer you want to remove: "))


# Traverse the whole array while mantaining a placing index that replaces the number if
# it is a number you want to have at the end we pop as many element as we swapped them
def remove_value_stable(N, x):
    i = j = 0
    while i < len(N):
        if N[i] != x:
            N[j] = N[i]
            j += 1

        i += 1

    while j < len(N):
        N.pop()
        j += 1


remove_value_stable(A, x)

print(A)
