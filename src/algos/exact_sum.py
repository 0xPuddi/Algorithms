#
# Given an array A sorted in non-decreasing order and a target value, write a
# function two_sum(A, t) that return True if there exist two elements A[i] and A[j]
# such that A[i] + A[j] = t and i != j, False otherwise. An optimal solution will
# run in only O(n) time.


# To make it run in O(n) time we have to consider the array as a matrix, where each
# row and column position is the sum between the two array elements. If we consider
# the weights position we know that the highest sum is in the bottom right corner,
# while the smallest one is in the top left corner, so if we start from the top right
# corner we know that all elements greater than the current one are located at the
# bottom and all elements that are less than it are in the left, instead if the target
# element is greater than the left neighbourd and smaller than the bottom neighbourd
# we traverse diagonally.
def exact_sum(A, t):
    r = 0
    c = len(A) - 1

    while r <= len(A) - 1 and c >= 0:
        current_sum = A[r] + A[c]

        if current_sum == t:
            # Exact target
            return True
        elif c - 1 >= 0 and t <= A[r] + A[c - 1]:
            # Smaller then left neighbor
            c = c - 1
        elif r + 1 <= len(A) - 1 and t >= A[r + 1] + A[c]:
            # Greater then bottom neighbor
            r = r + 1
        else:
            r = r + 1
            c = c - 1

    return False


if __name__ == "__main__":
    D = [1, 4, 5, 7, 8, 12, 34, 55, 67, 99]
    not_present = 96
    present = 60

    print(exact_sum(D, not_present))
    print(exact_sum(D, present))
