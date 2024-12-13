# Write a Python program to validate if a string is a valid palindrome, ignoring spaces and punctuation.

import string

# function to find whether string is valid or not
def isPallindrome(s):
    s = ''.join(c for c in s if c.isalnum()).lower()
    return s == s[::-1]

# calling a function
print(isPallindrome("Amit Kumar Yadav"))