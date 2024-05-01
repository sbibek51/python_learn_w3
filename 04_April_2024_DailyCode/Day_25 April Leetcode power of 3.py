'''
An integer n is a power of three, if there exists an integer x such that n == 3x.



Example 1:

Input: n = 27
Output: true
Explanation: 27 = 33
Example 2:

Input: n = 0
Output: false
Explanation: There is no x where 3x = 0.
Example 3:

Input: n = -1
Output: false
Explanation: There is no x where 3x = (-1).
'''

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n % 3 == 0:
            n /= 3
        return n == 1

obj = Solution()
print(obj.isPowerOfThree(9))
print(obj.isPowerOfThree(1))
print(obj.isPowerOfThree(2))
print(obj.isPowerOfThree(3))