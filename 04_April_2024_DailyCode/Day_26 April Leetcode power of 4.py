'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.
'''


class Solution(object):
    def isPowerOfFour(self, n):
        if n<=0:
            return False
        else:
            while n%4 ==0:
                n=n/4
            return n==1

obj = Solution()
print(obj.isPowerOfFour(4))
print(obj.isPowerOfFour(-1))
print(obj.isPowerOfFour(16))