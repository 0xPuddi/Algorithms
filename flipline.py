#!/usr/bin/python3
# Flipline:
# Write a program that reads a line from the standard input, and outputs that
# line flipped right-to-left.

# Time Complexity: O(n)
# Runs through the input string once.

# Space Complexity: O(n)
# It uses a string variable that grows with the input.

string = input("Insert a strig:\n")
reverse = ""
for i in range(len(string)):
    reverse += string[-i-1]
print(reverse)


# Time Complexity: O(n)
# Runs through the input string once.

# Space Complexity: O(1)
# It uses only an integer, prints on the same line.

l = input()
i = len(l)
while i > 0:
    i = i - 1
    print(l[i], end='')
print()
