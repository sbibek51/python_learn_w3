#Leet code problem solving daily

'''Valid pallindrome string:
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.



Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.'''

class Solution(object):
    def isPalindrome(self, s):
        s=s.lower()
        list_letters = []
        list_letters = ''.join(char for char in s if char.isalnum())
        rev_str = list_letters[::-1]
        if rev_str == list_letters:
            return True
        else:
            return False



obj = Solution()
print(obj.isPalindrome('race a car'))
print(obj.isPalindrome('rat a tar'))
