#!/usr/bin/python3
# Write a program that reads a text file from the standard input and outputs
# the most common word in the input. The words in the input are the maximal-length
# sequences of alphabetic characters. So, a word does not include spaces or
# punctuation characters. If two or more words appear more often, the program may
# print any one of them.

import os

# Time Complexity: O(n)
# Reading from the text file is not counted as the exercices thinks you will
# provide the text in the standard output. We traverse once the text to prepare
# each word, then we traverse once the array of words. O(2n) => O(n)

# Space Complexity: O(n)
# We store an array of words and a dictionary for each word. O(2n) => O(n)


# path = input("Enter the path for a text file: ") # Uncomment to provide custom txt file
path = "./data/commonword.txt"  # Comment to provide custom txt file
file = open(path, "r")
characters = ""

while 1:
    # read by character
    char = file.read(1)
    if not char:
        break
    else:
        characters += char

file.close()


def line_to_words(line):
    words = []
    w = ''

    for c in line:
        if c.isalpha():
            w += c
        else:
            if not w == '':
                words.append(w)
                w = ''
    if not w == '':
        words.append(w)

    return words


def commonword(W):
    # prepare text
    char_array = line_to_words(W)

    # traverse the file and cache the most used word
    most_used_word = char_array[0]
    most_used_counter = 1
    word_table = {
        most_used_word: most_used_counter
    }

    i = 1
    while i < len(char_array):
        word = char_array[i]
        # need init for fresh entry?
        if word in word_table:
            word_table[word] += 1
        else:
            word_table[word] = 1

        if word_table[word] > most_used_counter:
            most_used_word = word
            most_used_counter = word_table[word]

        i += 1

    print(most_used_word)


commonword(characters)
