# Consider the following algorithm that takes two strings A and B.
# You may assume that characters have numeric codes between 0 and
# m for some relatively small constant m. For example, ASCII characters
# are encoded by numbers between 0 and 127.

# Explain what algo_x does
# Write an algorithm called Better-Algo-X that does exactly the same
# thing as algo_x, but with a strictly better complexity.
# You can run better_x in linear time.

from src.algos.quick_sort import quick_sort


# The algo checks if string A contains B, thus B is a subset of A
# Complexity is O(n^2)
def algo_x(A, B):
    V = []
    for i in range(len(B)):
        V.append(0)

    for i in range(len(A)):
        x = False
        j = 0

        while j <= len(B) - 1 and x == False:
            if A[i] == B[j] and V[j] == 0:
                x = True
                V[j] = 1
            else:
                j = j + 1

    for j in range(len(B)):
        if V[j] == 0:
            return False

    return True


# Complexity: O(log(n))
def better_x_sort(A, B):
    quick_sort(A)
    quick_sort(B)

    if len(B) > len(A):
        return False

    i = j = 0
    while i < len(B):
        if j >= len(A):
            return False

        if A[j] == B[i]:
            i += 1
            j += 1
            continue

        j += 1

    return True


# Complexity: O(n)
# Since the alphabet is of fixed size we can also use an array
# to store each ASCII character using each character value as
# index
def better_x_hash(A, B):
    if len(B) > len(A):
        return False

    D = {}
    for j in range(len(B)):
        if B[j] not in D:
            D[B[j]] = 1
            continue

        D[B[j]] += 1

    for i in range(len(A)):
        if A[i] not in D:
            continue

        D[A[i]] -= 1

    for d in D:
        if D.get(d) > 0:
            return False

    return True


def string_to_ascii(A: list[str]) -> list[int]:
    return [ord(c) for c in A]


if __name__ == "__main__":
    print()

    A = "aabbbcc"
    B = "abbc"
    print(algo_x(string_to_ascii(A), string_to_ascii(B)))
    print(better_x_sort(string_to_ascii(A), string_to_ascii(B)))
    print(better_x_hash(string_to_ascii(A), string_to_ascii(B)))

    A = "aabbcc"
    B = "aaac"
    print(algo_x(string_to_ascii(A), string_to_ascii(B)))
    print(better_x_sort(string_to_ascii(A), string_to_ascii(B)))
    print(better_x_hash(string_to_ascii(A), string_to_ascii(B)))
