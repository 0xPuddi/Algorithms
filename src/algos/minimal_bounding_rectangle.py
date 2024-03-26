#!/usr/bin/python3
# Consider a sequence of n points p1, p2, p3, ... in a plane identified by their
# Cartesian coordinates. The coordinates are given in the form of two arrays X and
# Y both containing of n numbers, such that point pi has coordinates X[i] and Y[i].
# Write a function called minimal_bounding_rectangle_area(X,Y) that, given two arrays
# of coordinates X and Y representing n points, returns the area of the smallest
# axis-aligned rectangle that covers all the n points. An axis-aligned rectangle is
# such that its sides are parallel to the or axis.

# Time Complexity: O(n)
# We traverse the array once two times, giving O(2n) = O(n)

# Space Complexity: O(1)
# We store 4 integers, giving O(4) = O(1)


A = []
# Uncomment to provide custom arrays
# arr1 = input("Enter the first arrays of points separated by a space: ")
# Uncomment to provide custom arrays
# arr2 = input("Enter the swcond arrays of points separated by a space: ")
# Uncomment to provide custom arrays
# a = [[int(n) for n in arr1.split(" ")],[int(n) for n in arr2.split(" ")]]
# Uncomment to provide custom arrays
# A.append(a)


A.append([[3, 2, 10, 4], [5, 5, 3, 2]])
A.append([[2], [89]])
A.append([[-8, 8, 9, -9, 4, -4, 4, -9, 7], [10, 1, -1, -5, 7, -7, -2, 0, 3]])


def minimal_bounding_rectangle(X, Y):
    if len(X) < 2 or len(Y) < 2 or len(X) != len(Y):
        return None

    max_x = X[0]
    min_x = X[0]
    max_y = Y[0]
    min_y = Y[0]

    for i in range(len(X)):
        if X[i] > max_x:
            max_x = X[i]

        if X[i] < min_x:
            min_x = X[i]

    for i in range(len(Y)):
        if Y[i] > max_y:
            max_y = Y[i]

        if Y[i] < min_y:
            min_y = Y[i]

    return (abs(min_x) + abs(min_x)) * (abs(min_y) + abs(max_y))


for a in A:
    print(minimal_bounding_rectangle(a[0], a[1]))
