
# You get two non decreasing sorted arrays A and B and a value t, return
# true if there is the exact sum of t between elements of A and B,
# otherwise return false.

# Same as exact_sum we traverse the two arrays as a matrix
def exact_sum_AB(A, B, t):
    r = 0
    c = len(A) - 1

    while r <= len(B) - 1 and c >= 0:
        if A[c] + B[r] == t:
            return True
        elif c - 1 >= 0 and t <= A[c - 1] + B[r]:
            c -= 1
        elif r + 1 <= len(B) - 1 and t >= A[c] + B[r + 1]:
            r += 1
        else:
            r += 1
            c -= 1

    return False


if __name__ == "__main__":
    A = [1, 3, 4, 6, 7, 12, 34, 67, 88, 123, 234]
    B = [1, 5, 6, 9, 12, 13, 14, 16, 22, 34, 66, 78, 56, 88, 90]
    present = 91
    not_present = 51

    print(exact_sum_AB(A, B, present))
    print(exact_sum_AB(A, B, not_present))
