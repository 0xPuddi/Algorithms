#!/usr/bin/python3
# Take two ordered lists and merge them together, do it twice: with and without
# duplicates

# Time Complexity: O(n)
# We run through both the arrays once, thus O(2n) = O(n)

# Space Complexity: O(N)
# We store the merged array


def merge(A, B):
    i = j = 0
    X = []

    while i < len(A) or j < len(B):
        if i >= len(A):
            X.append(B[j])
            j = j + 1
            continue

        if j >= len(B):
            X.append(A[i])
            i = i + 1
            continue

        if A[i] <= B[j]:
            X.append(A[i])
            i = i + 1
        elif A[i] > B[j]:
            X.append(B[j])
            j = j + 1

    return X


if __name__ == "__main__":
    A = []
    B = []
    # Uncomment to provide custom arrays
    # array = input("Insert integers separated by spaces: ")
    # A = [int(n) for n in array.split(" ")]
    # array2 = input("Insert integers separated by spaces: ")
    # B = [int(n) for n in array2.split(" ")]

    # Comment to provide custom arrays
    A = [2, 4, 5, 6, 23, 45, 67, 67, 89, 99]
    B = [1, 3, 56, 77, 88, 123, 124, 125]

    print(merge(A, B))
