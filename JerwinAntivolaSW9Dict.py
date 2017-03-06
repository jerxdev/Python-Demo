import sys
import string
x = input("Enter a sentence")

x = x.lower()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

letter_count = {}
for char in x:
    if char in alphabet:
        if char in letter_count:
            letter_count[char] = letter_count[char] + 1
        else:
            letter_count[char] = 1

keys = letter_count.keys()
keys2 = sorted(keys)
for char in keys2:
    print(char, letter_count[char])
