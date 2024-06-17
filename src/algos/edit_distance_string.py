

# Given two strings and operations:
# Insert, Delete and Modify
# find the minomum number of operations or edits required
# to convert the first string to the second one

import math


def minimum_edit_distance_obsolete(s1, s2):
    ed = 0

    r = c = 0
    while r < len(s2) or c < len(s1):
        if r > len(s2):
            c += 1
            ed += 1
        elif c > len(s1):
            r += 1
            ed += 1
        elif s2[r] != s1[c]:
            ed += 1
            r += 1
            c += 1
        else:
            r += 1
            c += 1

    return ed


def minimum_edit_distance_dinamic(s1: str, s2: str) -> int:
    # Build the chache matrix: each element represent a graph edge
    cache = [[math.inf] * (len(s2) + 1) for i in range(len(s1) + 1)]

    # We fill the bottom row from left (total cost to pay from
    # the end of the graph, which is the bottom right to that
    # point) to right
    for j in range(len(s2) + 1):
        cache[len(s1)][j] = len(s2) - j

    # We fill the top right column from top (total cost to pay from
    # the end of the graph, which is the bottom right to that
    # point) to bottom
    for i in range(len(s1) + 1):
        cache[i][len(s2)] = len(s1) - i

    # We move from the previous to last row and column position backwards:
    # Each time the string has the same character we move diagonally and
    # we cache diagonally the cost we have collected until there, if there
    # is no diagonal movement to do each position will have smallest of the
    # cost of each three neighbourds on its south-est, then if there are
    # no equal characters each diagonal position will have the total cost
    # that we have to spend from the end until that point
    for i in range(len(s1) - 1, -1, -1):
        for j in range(len(s2) - 1, -1, -1):
            if s1[i] == s2[j]:
                cache[i][j] = cache[i + 1][j + 1]
            else:
                cache[i][j] = 1 + min(cache[i + 1][j],
                                      cache[i][j + 1], cache[i+1][j+1])

    return cache[0][0]


if __name__ == "__main__":
    print(minimum_edit_distance_obsolete("Lugano", "Zurigo"))
    print(minimum_edit_distance_obsolete("xabcd", "abcdy"))

    print(minimum_edit_distance_dinamic("Lugano", "Zurigo"))
    print(minimum_edit_distance_dinamic("xabcd", "abcdy"))
