'''Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
 '''


class Solution(object):
    def missingNumber(self, nums):
        nums.sort()
        max_num = len(nums)
        sum = (max_num * (max_num + 1) / 2)  # sum of n terms
        sum1 = 0
        for i in range(0, len(nums)):
            sum1 = sum1 + nums[i]
        return sum - sum1


obj = Solution()
# nums = [0,1,2,4]
nums = [0,1]
print(obj.missingNumber(nums))