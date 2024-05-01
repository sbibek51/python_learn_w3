#Bibek Shiwakoti

'''

Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.



Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false

'''


class Solution(object):
    def isPowerOfTwo(self, n):
        if n<=0:
            return False
        else:
            return (n & (n-1)) ==0   #if n is power of two there is only one 1 bit on
        #doing and leaves with all 0 else it will result at least one 1

obj = Solution()
print(obj.isPowerOfTwo(8))
print(obj.isPowerOfTwo(1))
print(obj.isPowerOfTwo(3))




# Control shift alt and L to format a code