#!/usr/bin/python3
# Write a program that reads a sequence of ordered space-separated values from the
# input and outputs a "compressed"; version of the input sequence. The
# compression is obtained by transforming a sequence of three or more identical
# elements as X * N, where X is the element and N is the number of consecutive
# copies of X.

# Time Complexity: O(n)
# The functions both run one time over the whole list

# Space Complexity: compress == O(N), compress_v2 == O(1)
# compress uses a cache that can grow as much as the input list in the worst case
# compress_v2 stores only a few number variables


A = input("Enter numbers separated by spaces: ")
A = A.split()
A = [int(n) for n in A]


# For
def compress(N):
    cache = []

    for i in range(1, len(N) + 1):
        cache.append(N[i - 1])

        if i != len(N):
            if cache[0] == N[i]:
                continue
            else:
                if len(cache) < 3:
                    for j in range(len(cache)):
                        print(cache[j])
                else:
                    print(str(cache[0])+" * "+str(len(cache)))
                cache = []
        else:
            if len(cache) < 3:
                for j in range(len(cache)):
                    print(cache[j])
            else:
                if cache[0] == cache[-1]:
                    print(str(cache[0])+" * "+str(len(cache)))
                else:
                    print(str(cache[0])+" * "+str(len(cache) - 1))
                    print(cache[-1])


# While
def compress_v2(A):
    i = 0
    while i < len(A):
        j = i + 1
        while j < len(A) and A[j] == A[i]:
            j = j + 1
        if j - i <= 2:
            for _ in range(j - i):
                print(A[i])
        else:
            print(A[i], '*', j - i)
        i = j


# Runs
compress(A)
print()
compress_v2(A)
