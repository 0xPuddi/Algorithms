#!/usr/bin/python3
# Calculate the square root of a number using only basic operations such as addition,
# multiplication, subtraction and division. It must run in log(n) time.

# Space complexity: O(log(n))
# We do a binary search over the gap between 1 and n

# Space complexity: O(1)
# We store only few integers

def square_root(x):
    if x < 0:
        raise ValueError("Square root is not defined for negative numbers")
    if x < 1:
        left, right = x, 1.0
    else:
        left, right = 1.0, x

    epsilon = 1e-6  # Adjust this for desired precision

    while right - left > epsilon:
        mid = (left + right) / 2
        mid_sq = mid * mid

        if mid_sq == x:
            return mid
        elif mid_sq < x:
            left = mid
        else:
            right = mid

    return left


if __name__ == "__main__":
    print(square_root(17))
