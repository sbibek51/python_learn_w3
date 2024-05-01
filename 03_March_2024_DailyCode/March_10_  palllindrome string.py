"""Q1: A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"

Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"

Output: false

Explanation: "raceacar" is not a palindrome."""


def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

    return cleaned_string == cleaned_string[::-1]


# Test the function
print(is_palindrome("A man, a plan, a canal, Panama!"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))