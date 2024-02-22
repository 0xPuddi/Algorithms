#!/usr/bin/python3
# Leap Year:
# Write a function leap_year(y) that, given a year number in the Gregorian calendar,
# return True if is a leap year, or False otherwise. Recall that a leap year is one
# whose number is divisible by 4, excluding the year numbers divisible by 100, but
# including the year numbers divisible by 400.

# Time Complexity: O(1)
# Only conditional statements

# Space Complexity: O(1)
# It uses zero variables

# leap_year
def leap_year(n):
    if n % 4 == 0:
        if n % 400 == 0:
            return True
        if n % 100 == 0:
            return False

        return True

    return False


# Runs
print(leap_year(2000))
print(leap_year(1969))
print(leap_year(2023))
print(leap_year(1984))
print(leap_year(2022))
print(leap_year(2200))
print(leap_year(2400))
print(leap_year(1900))
