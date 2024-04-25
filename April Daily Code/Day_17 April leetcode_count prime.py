class Solution(object):
    def countPrimes(self, n):
        count =0
        for i in range(2,n):
            is_prime = True
            for j in range(2,i):
                if i%j==0:
                    is_prime = False
                    break
            if is_prime:
             count = count +1
        return count

obj = Solution()
print(obj.countPrimes(10))