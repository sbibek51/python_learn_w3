# Bibek Shiwakoti
"""

forward and backward. Alphanumeric characters include letters and numbers. Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: s = "A man, a plan, a canal: Panama"

Output: true

Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"

Output: false

Explanation: "raceacar" is not a palindrome.

"""


def is_palindrome(s):
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
    rev_str = cleaned_string[::-1]
    #     print(cleaned_string)
    return cleaned_string == rev_str


# Test the function
print(is_palindrome("A man, a plan, a canal, Panama!"))
print(is_palindrome("racecar"))
print(is_palindrome("hello"))



# control shift alt and L to format a code in Pycharm