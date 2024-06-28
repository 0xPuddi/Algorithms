# Let two numbers a, b define an interval, that is, the set of all numbers x such
# that a ≤ x ≤ b or b ≤ x ≤ a. Write an algorithm Compare-Intervals(a1, b1, a2, b2) that compares
# the two intervals, I1 defined by a1 and b1, and I2 defined by a2 and b2. The algorithm should return
# “disjoint” if the two intervals are disjoint, meaning that there are no numbers that are in both I1
# and I2; or “1 equals 2” if the two intervals are identical, meaning that all the numbers in I1 are also
# in I2 and vice-versa; or “1 covers 2” if all the numbers in I2 are also in I1 but not vice-versa; or “2
# covers 1” if all the numbers in I1 are also in I2 but not vice-versa; or “partial” if more than one
# number is in both I1 and I2, but there are also numbers in I1 that are not in I2 and vice-versa; or
# “touch” if there is exactly one number that is in both I1 and I2, and there are also other numbers in
# I1 that are not in I2 and vice-versa. For example, Compare-Intervals(−2.3, 2, 0, −7) must return
# “partial”, because the interval [−2.3, 0] is in both intervals [−2.3, 2] and [−7, 0], but there are also
# other elements in both; and Compare-Intervals(5.5, 6.6, 7, 5.2) must return “2 covers 1”, because
# the first interval, [5.5, 6.6] is completely contained in the second interval [5.2, 7], and the second
# interval has other numbers that are not in the first.


import numpy as np
import time
import matplotlib.pyplot as plt
from src.algos.quick_sort import quick_sort


# Complexity: O(1)
def compare_intervals(a: int, b: int, c: int, d: int):
    if b < a:
        a, b = b, a
    if d < c:
        c, d = d, c

    if a == c and c == d:
        return "AB equals CD"  # If the two intervals are identical

    if c <= a and b <= d:
        return "CD covers AB"  # If all numbers of AB are aslo in CD but not in vice-versa

    if a <= c and d <= b:
        return "AB covers CD"  # If all numbers of CD are aslo in AB but not in vice-versa

    if (a == d and a <= b) or (b == c and c <= d):
        return "Touch"  # If there is only one element that is in both AB and CD

    if (a > d) or (c > b):
        return "Disjoint"  # There are no numbers that are in both AB and CD

    if (a < c and b > c) or (b > d and a < d):
        return "Partial"  # If more than one number is in both AB and CD but there are aslo number only in one interval

    return "Error"


if __name__ == "__main__":
    print(compare_intervals(-2.3, 2, 0, 7))
    print(compare_intervals(5.5, 6.6, 7, 5.2))
    print(compare_intervals(4, -2, 2, -2))
