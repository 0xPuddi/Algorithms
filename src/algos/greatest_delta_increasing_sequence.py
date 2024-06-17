#!/usr/bin/python3
# Write an algorithm that calculates the greatest delta of an
# increasing sequence inside a list

A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 10
B = [1]
# False
C = [1, 2]
# 1
D = [1, 2, 3, 4, 5, 6, 7, 2, 6, 17, 44, 2]
# 42

# Time Complexity: O(n)
# We loop throught the array linearly

# Space Complexity: O(1)
# We store only three integers


def greatest_delta_increasing_sequence(A):
    if len(A) <= 1:
        return False

    maxDelta = 0
    start = 0
    end = 0

    for i in range(1, len(A)):
        if A[end] < A[i]:
            end = i
        elif A[end] - A[start] > maxDelta:
            maxDelta = A[end] - A[start]
            start = end = i

        if i == len(A) - 1:
            if A[end] - A[start] > maxDelta:
                maxDelta = A[end] - A[start]

    return maxDelta


if __name__ == "__main__":
    print(greatest_delta_increasing_sequence(A))
    print(greatest_delta_increasing_sequence(B))
    print(greatest_delta_increasing_sequence(C))
    print(greatest_delta_increasing_sequence(D))
