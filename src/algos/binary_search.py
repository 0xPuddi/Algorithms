#!/usr/bin/python3
# Binary search

# Time Complexity: O(log(n))
# Binary search, each time it divides the element to search in by half

# Space Complexity: O(1)
# We use only four variables, two bools and two integers.


def binary_search(A, x):
    l = 0
    r = len(A)

    while l < r:
        p = (l + r) // 2
        if A[p] == x:
            return True
        elif A[p] < x:
            l = p + 1
        elif A[p] > x:
            r = p

    return False


if __name__ == "__main__":
    array = input("Insert integers separated by spaces: ")
    A = [int(n) for n in array.split(" ")]
    x = int(input("Insert integer you want to remove: "))

    print(binary_search(A, x))
