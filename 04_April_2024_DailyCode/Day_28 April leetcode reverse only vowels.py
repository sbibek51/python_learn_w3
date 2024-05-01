'''Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.



Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"'''


class Solution(object):
    def reverseVowels(self,s):
        vowels = 'aeiouAEIOU'
        s=list(s)
        left =0
        right = len(s)-1
        while left<right:
            while left<right and s[left] not in vowels:
                left = left +1
            while left<right and s[right] not in vowels:
                right = right -1

            s[left],s[right] = s[right],s[left]
            left= left +1
            right = right-1
        return ''.join(s)

obj =Solution()
s = "leetcode"
print(obj.reverseVowels(s))